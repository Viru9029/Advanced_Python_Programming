"""
4. Now, add a line in your mymod module that calls the test function automatically only when the module
is run as a script, not when it is imported The line you add will probably test the
value of __name__ for the string "__main__", as shown in this unit. Try running your module from the
system command line; then, import the module and test its functions interactively.
"""
import mymod

print(__name__)
if __name__ == "__main__":
    print("Correct Output")
else:
    print("Wrong Output")
