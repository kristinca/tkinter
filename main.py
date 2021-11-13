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




# Documenting specification requirements

# The purpose of the specification is:
# To give EVERYONE INVOLVED IN THE PROJECT a point of REFERENCE for what the developer will create.
# It spells out:
# 1. the problem to be solved
# 2. the functionality required
# 3. the scope of what the program should and shouldn't do.


# Contents of a simple specification:

# 1. Description: One / two sentences,
# describe the primary purpose, function, and goals of the application (the program's mission statement).

# 2. Functionality required: A list of specific things
# the program needs to be able to do to be minimally functional.
# Includes both hard requirements-detailed output and input formats, and
# soft requirements—goals that are not quantifiable attainable, but that the program should strive toward.

# 3. Functionality not required: A list of things the program does not need to do.
# It exists to clarify the scope of the software,
# and make sure NOBODY EXPECTS unreasonable things from the application.

# 4. Limitations: A list of constraints under which the program must operate, both technological and human.

# 5. Data dictionary: A detailed list of the data fields
# the application will deal with and their parameters.
# These can get quite lengthy but are a CRITICAL REFERENCE
# as the application expands and the data gets utilized in other contexts.
