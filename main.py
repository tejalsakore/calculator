from ast import Expression
from tkinter import *

#creating basic window
window=Tk()
window.geometry("312x324")
window.resizable(0,0) #this prevents from resizing the window
window.title("Calculator")

# functions

# 'btn_click()' continuously updates the input field whenever you enter the number
def btn_click(item):
    global expression 
    expression = expression + str(item)
    input_text.set(expression)

#'btn_clear()' clears the input field
def btn_clear():
    global expression
    expression = " "
    input_text.set(" ")

#'btn_equal' calculates the expression present in input field
def btn_equal():
    global expression
    result = str(eval(expression)) #eval() evaluates the string expression directly
    input_text.set(result)
    expression = " "

expression = " "
# 'StringVar()' is used to get the instance of input field
input_text = StringVar()

# creating a frame for the input field
input_frame = Frame(window,width = 312, height = 50,bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side =TOP)

# creating a input field inside the 'Frame'
input_field = Entry(input_frame, font =('arial',18,'bold'), textvariable = input_text, width = 50, bg= "#eee",bd =0,justify=RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10) # 'ipady' is internal padding to increase the height of input field

# creating another 'Frame' for the button below the 'input_frame'
btns_frame = Frame(window,width = 312,height = 272.5,bg = "grey")
btns_frame.pack()

# first row
clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0 ,bg = "#eee", cursor = "hand2", command = lambda : btn_clear()).grid(row=0,column=0,columnspan =3,padx=1,pady=1)  
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0 ,bg = "#eee", cursor = "hand2", command = lambda : btn_click("/")).grid(row=0,column=3,padx=1,pady=1)
mainloop()