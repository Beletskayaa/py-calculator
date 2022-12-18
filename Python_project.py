#!/usr/bin/env python
# coding: utf-8

# In[45]:


from tkinter import *
import math 

################ ФУНКЦИИ ################

def btn_press(operand):
    global expression
    expression += str(operand)
    display.set(expression)

def press_ac():
    global expression
    expression = ""
    display.set("")

def press_del():
    global expression
    expression = expression[:-1]
    display.set(expression)

def press_eq():
    global expression
    result = str(eval(expression))
    display.set(result)
    expression = ""
    
def sqrt_exp():
    global expression
    result = str(math.sqrt(eval(expression)))
    display.set(result)
    expression = result
                 
def deg_exp():
    global expression
    result = str(eval(expression) * eval(expression))
    display.set(result)
    expression = result
    
def sin_exp():
    global expression
    result = str(math.sin(math.radians(eval(expression))))
    display.set(result)
    expression = result

def cos_exp():
    global expression
    result = str(math.cos(math.radians(eval(expression))))
    display.set(result)
    expression = result
    
def tan_exp():
    global expression
    result = str(math.tan(math.radians(eval(expression))))
    display.set(result)
    expression = result
    
def fact_exp():
    global expression
    result = str(math.factorial(eval(expression)))
    display.set(result)
    expression = result
    
def ln_exp():
    global expression
    result = str(math.log1p(eval(expression)))
    display.set(result)
    expression = result
    
def log_exp():
    global expression
    result = str(math.log10(eval(expression)))
    display.set(result)
    expression = result
    
    
    
################ РАЗМЕР ОКОШКА И ПОЛЕ ВВОДА ################

root = Tk()
root.geometry("478x565+200+200")
root.title("Калькулятор")

expression = ""
display = StringVar()
expression_field = Entry(textvariable=display, justify=RIGHT)
expression_field.grid(columnspan = 4, ipadx = 60)

################ КНОПКИ ОПЕРАЦИЙ ################

btn_ac = Button(root, text = 'AC', height = 4, width = 11, command = lambda: press_ac())
btn_ac.grid(row = 1, column = 1)

btn_del = Button(text = 'DEL', height = 4, width = 11, command = lambda: press_del())
btn_del.grid(row = 1, column = 2)

btn_point = Button(text = '.', height = 4, width = 11, command = lambda: btn_press('.'))
btn_point.grid(row = 1, column = 3)

btn_div = Button(text = '/', height = 4, width = 4, command = lambda: btn_press('/'))
btn_div.grid(row = 1, column = 4)

btn_mult = Button(text = '*', height = 4, width = 4, command = lambda: btn_press('*'))
btn_mult.grid(row = 2, column = 4)

btn_min = Button(text = '-', height = 4, width = 4, command = lambda: btn_press('-'))
btn_min.grid(row = 3, column = 4)

btn_plus = Button(text = '+', height = 4, width = 4, command = lambda: btn_press('+'))
btn_plus.grid(row = 4, column = 4)

btn_eq = Button(text = '=', height = 4, width = 11, command = lambda: press_eq())
btn_eq.grid(row = 7, column = 3)

btn_sqrt = Button(text = 'sqrt', height = 4, width = 11, command = sqrt_exp)
btn_sqrt.grid(row = 5, column = 1)

btn_deg = Button(text = '^2', height = 4, width = 11, command = deg_exp)
btn_deg.grid(row = 5, column = 3)

btn_sin = Button(text = 'sin', height = 4, width = 11, command = sin_exp)
btn_sin.grid(row = 6, column = 1)

btn_cos = Button(text = 'cos', height = 4, width = 11, command = cos_exp)
btn_cos.grid(row = 6, column = 2)

btn_tan = Button(text = 'tan', height = 4, width = 11, command = tan_exp)
btn_tan.grid(row = 6, column = 3)

btn_fact = Button(text = 'x!', height = 4, width = 4, command = fact_exp)
btn_fact.grid(row = 6, column = 4)

btn_ln = Button(text = 'ln', height = 4, width = 11, command = ln_exp)
btn_ln.grid(row = 7, column = 1)

btn_log = Button(text = 'log', height = 4, width = 11, command = log_exp)
btn_log.grid(row = 7, column = 2)

################ КНОПКИ ЦИФР ################

btn_1 = Button(text = '1', height = 4, width = 11, command = lambda: btn_press(1))
btn_1.grid(row = 2, column = 1)

btn_2 = Button(text = '2', height = 4, width = 11, command = lambda: btn_press(2))
btn_2.grid(row = 2, column = 2)

btn_3 = Button(text = '3', height = 4, width = 11, command = lambda: btn_press(3))
btn_3.grid(row = 2, column = 3)

btn_4 = Button(text = '4', height = 4, width = 11, command = lambda: btn_press(4))
btn_4.grid(row = 3, column = 1)

btn_5 = Button(text = '5', height = 4, width = 11, command = lambda: btn_press(5))
btn_5.grid(row = 3, column = 2)

btn_6 = Button(text = '6', height = 4, width = 11, command = lambda: btn_press(6))
btn_6.grid(row = 3, column = 3)

btn_7 = Button(text = '7', height = 4, width = 11, command = lambda: btn_press(7))
btn_7.grid(row = 4, column = 1)

btn_8 = Button(text = '8', height = 4, width = 11, command = lambda: btn_press(8))
btn_8.grid(row = 4, column = 2)

btn_9 = Button(text = '9', height = 4, width = 11, command = lambda: btn_press(9))
btn_9.grid(row = 4, column = 3)

btn_10 = Button(text = '0', height = 4, width = 11, command = lambda: btn_press(0))
btn_10.grid(row = 5, column = 2)

btn_11 = Button(text = 'pi', height = 4, width = 4, command = lambda: btn_press(math.pi))
btn_11.grid(row = 7, column = 4)

btn_12 = Button(text = 'e', height = 4, width = 4, command = lambda: btn_press(math.e))
btn_12.grid(row = 5, column = 4)

root.mainloop()


# In[ ]:





# In[ ]:




