"""
7. Experiment with module reloads: perform the tests in the changer.py example,
changing the called function’s message and/or behavior repeatedly, without stopping
the Python interpreter. Depending on your system, you might be able to edit changer in another window.
"""
import changer
changer.multiply(5,5)
print("\n")

import importlib
importlib.reload(changer)
changer.division(25,5)