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


