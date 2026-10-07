#print(dir())
# `if __name__ == "__main__"` Idiom

# `__name__` is a **special variable** whose value Python sets based on how the module is used.

# ### When file is run directly

#     python calculator.py

# Python sets:

#     __name__ = "__main__"

# So:

#     if __name__ == "__main__":
#         print("Running directly")

# will execute.

# ### When file is imported

#     import calculator

# Python sets:

#     __name__ = "calculator"

# Therefore:

#     if __name__ == "__main__":

# is `False`, so that block does not run.

# ### Why use it?

# It separates:

# - **Reusable code** → functions/classes that can be imported
# - **Main code** → code that should run only when the file is executed directly

# > **Run directly → `__name__ == "__main__"` → main code runs.**  
# > **Imported → `__name__ == module name` → main block does not run.**

# ### Important

# Without this condition, **top-level code in a module executes when the module is imported**.

# **Main purpose:** prevent demo, test, or execution code from running automatically during import.
print(__name__)
def display(name):
    return name
def do_something():
    print("This function is doing something ")
if __name__ =="__main__":
    print("This is nameMain.py ")
    name=input("enter you name:")
    print(display(name))
    do_something()