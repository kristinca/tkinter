"""

   My notes and work from the book
'Python GUI Programming with Tkinter'
        by Alan D. Moore

"""

# Star imports (from module import *) are seen often in Python tutorials and example code,
# but in production code they should be AVOIDED.
# Python modules can contain ANY number of classes, functions, or variables;
# when you do a star import, you import ALL of them,
# which can lead to one import overwriting the objects imported from another module.

# The Frame class is a generic Tk widget that is typically used as a container for other widgets.
# We can add any number of widgets to the Frame class,
# then treat the whole thing as though it were a single widget.


# Tkinter has a collection of variable types including StringVar, IntVar, DoubleVar, and BooleanVar.

# Tkinter variables have special functionality that regular Python variables lack, as:
# the ability to automatically propagate changes to all the widgets
# that reference them or trigger an event when they're changed.

# tkinter variables -> set() , get()

# hello world app:
# We start building our view by creating a Label object and Entry
# the Entry object gets a new argument: textvariable.
# By passing a Tkinter StringVar variable to this argument,
# the contents of the Entry box will be bound to the variable,
# and we can access it without needing to reference the widget.

# the columnconfigure() method is used to make changes to a widget's grid columns

#self.title(): -> sets the window title
# self.geometry(): -> sets the size of our window in pixels,
# in the format x * y (width x height).
# self.resizable(): -> sets whether the program window can be resized (True or False)
