import os
import random as r
from tkinter import *

#Tkinter init
root = Tk()
root.title("Password Generator")

#GLOBAL VARIABLES
password_lenght = 1
small_c_var = IntVar()
big_c_var = IntVar()
numbers_c_var = IntVar()
diac_c_var = IntVar()

#generator
def gen_diacrit():
    numbers = []
    y,x,z = r.randrange(33,48),r.randrange(58,65),r.randrange(123,127)
    numbers.extend([x,y,z])
    symbol = chr(numbers[r.randrange(0, len(numbers)-1)])
    return symbol

#controler
def confirm():
    global slider
    global password_lenght
    
    password_lenght = slider.get()
    number_entry.delete(0, END)
    number_entry.insert(0, password_lenght)
 
    
def generator(small, big, digits, other, lenght):
    global result
    
    num = small.get() + big.get() + digits.get() + other.get() 
    result.delete(0, END)
    result_string = ""
    while len(result_string) != lenght and len(result_string) < lenght and num != 0:
        if small.get() == 1:
            result_string += chr(r.randrange(97,123))
        if big.get() ==1:
            result_string += chr(r.randrange(65, 91))
        if digits.get() == 1:
            result_string += str(r.randrange(0,10))  
        if other.get() == 1:
            result_string += gen_diacrit() 
    if num != 0:       
        result.insert(0, ''.join(r.sample(result_string,lenght)))
        
               
#FRAMES
##frames_init
frame_length = LabelFrame(root)
frame_options = LabelFrame(root, text= "Password Setup")
frame_result = LabelFrame(root, text = "Password Generator")

##frame_lenght
lenght_label = Label(frame_length, text ="Password lenght")
number_entry = Entry(frame_length, width = 2, borderwidth = 4)
slider  =  Scale(frame_length, from_ = 1, to = 24, orient = HORIZONTAL,sliderlength = 20,length= 65,borderwidth = 3)
confirm = Button(frame_length, text= "Confirm", command = confirm)
number_entry.insert(0, password_lenght)

##frame_options
small_c= Checkbutton(frame_options, text = "Letters (a-z)", variable = small_c_var)
big_c = Checkbutton(frame_options, text = "Letters (A-Z)",variable = big_c_var)
numbers_c = Checkbutton(frame_options, text = "Digits (0-9)",variable = numbers_c_var) 
diac_c = Checkbutton(frame_options, text = "Other characters", variable = diac_c_var)

##frame_result
result = Entry(frame_result, text="your password", width = 30, borderwidth = 5) 
result_button = Button(frame_result,text="Generate", command = lambda:generator(small_c_var,big_c_var,numbers_c_var,diac_c_var,password_lenght))


#RENDERING
##frame_lenght
frame_length.pack(anchor = W ,padx = 10, pady = 5)
lenght_label.grid(column = 0, row = 0)
number_entry.grid(column = 1, row = 0)
slider.grid(column = 1, row = 1)
confirm.grid(column = 0, row = 1)

##frame_options
frame_options.pack(anchor = W,padx = 10, pady = 5)
small_c.pack(anchor = W)
big_c.pack(anchor = W)
numbers_c.pack(anchor = W)
diac_c.pack(anchor = W)

##frame_result
frame_result.pack(anchor = W,padx = 10, pady = 5)
result.pack()
result_button.pack()

#mainloop
root.mainloop()