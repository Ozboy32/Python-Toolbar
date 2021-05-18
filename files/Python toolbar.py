# imports
from tkinter import *
import time
import os
import linecache
from PIL import Image, ImageTk
from functools import partial

# variables
win = Tk()
widget_num = open("widget_num.txt", "r")
app = open("program.txt", "r")
pic = open("image.txt", "r")
programs = {}
images = {}

#canvas
cv = Canvas(width=1920, height=50, highlightthickness=0)
cv.pack(side='top', fill='both', expand='yes')

# Attributes
win.overrideredirect(True)  # Make the window borderless
win.attributes('-alpha', 0.8)  # Make the window transparent
win.attributes('-topmost', True)  # Always on top
win.configure(bg="#32a852")  # bg colour
# win.geometry("50x1080+1230+0")  # right side, make sure you also change the inBox() and outBox() functions to match
win.geometry("1920x50+0+-48")  # top

# functions
def inBox(event):  # expand the toolbar
    time.sleep(0.3)
    win.geometry("1920x50+0+0")


def outBox(event):  # collapse the toolbar
    win.geometry("1920x50+0+-48")


def open(program):  # open the program
    time.sleep(0.15)
    os.startfile(program)


win.bind('<Enter>', inBox)  # bind mouse entry
win.bind('<Leave>', outBox)  # bind mouse exit

# create widgets from file
for x in widget_num:
    # setup dictionary's
    programs["program%s" % x[:-1]] = str(app.readline())[:-1]   # add current program to dict
    images["image%s" % x[:-1]] = str(pic.readline())[:-1]   # add current image to dict
    print(programs["program%s" % x[:-1]])   # test that the dict works (debug)
    print(images["image%s" % x[:-1]])   # test that the dict works (debug)

    # create usable image
    image1 = Image.open(images["image%s" % x[:-1]])     # get image location from dict
    image2 = image1.resize((40, 40))    # resize the image
    images["image%s" % x[:-1]] = ImageTk.PhotoImage(image2)     # reassign the dict

    # create program variable from dict
    program = programs["program%s" % x[:-1]]

    # create the button
    widget = Button(cv, height=40, width=40, image=images["image%s" % x[:-1]], command=partial(open, program))

    # pack the button
    widget.pack(side=LEFT, padx=5, pady=2)


# close files
widget_num.close()
app.close()
pic.close()

win.mainloop()
