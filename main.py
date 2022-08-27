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

