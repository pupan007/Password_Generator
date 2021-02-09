import os
from tkinter import *
from PIL import ImageTk, Image

#Tkinter init
root = Tk()
root.title('Image Viewer')

#images loader
i=0
directory = 'images/' 
images = []
for image in os.listdir(directory):
    if image.endswith(".png") or image.endswith(".jpg"):
        img = ImageTk.PhotoImage(Image.open(directory+image))
        images.append(img)
        
#1st photo init
photo = Label(image = images[i])
photo.grid(row = 0, column= 0, columnspan = 3)

#utils
def forward(len):
    global photo
    global i
    global button_forward
    global button_backward

    i += 1
    photo.grid_forget()
    photo = Label(image = images[i])
    photo.grid(row = 0, column= 0, columnspan = 3)
    if i == len:
        button_forward['state'] = DISABLED
    if i != 0:
        button_backward['state'] = NORMAL
    

def backward(len):
    global photo
    global i
    global button_backward
    i -= 1
    photo.grid_forget()
    photo = Label(image = images[i])
    photo.grid(row = 0, column= 0, columnspan = 3)
    if i == 0:
        button_backward['state'] = DISABLED
    

#buttons
button_backward = Button(root, text= "<<",padx = 50, command = lambda: backward(len(images)-1))
if i == 0:
    button_backward['state']= DISABLED
button_exit = Button(root, text = "Exit Program",command =root.quit,padx = 50)
button_forward = Button(root, text=">>",padx = 50, command = lambda: forward(len(images)-1))


#photo and button rendering
button_backward.grid(row = 1, column= 0)
button_exit.grid(row =1, column= 1)
button_forward.grid(row = 1, column= 2)

root.mainloop()
