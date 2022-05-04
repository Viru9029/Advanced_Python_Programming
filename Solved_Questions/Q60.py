"""
6. Package imports. Finally, import your file from a package. Create a subdirectory called mypkg nested in a
directory on your module import search path, move the mymod_1.py module file you created in exercises 2 or 4
into the new directory, and try to import it with a package import of the form: import mypkg.mymod.
"""
import mypkg
import mypkg.subtract
mypkg.subtract.subtract1(30, 10)
print("\n")

import mypkg.mymode.mymod_1 as a
a.test(r"V:\PG-DAI\1.Python\Day 12\Exercise No 6\Lab_Exercise_5.txt")