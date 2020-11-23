# regular expressions in python (RegEx)
import re

# search string for match or no match
text = "You can start learning Python."
x = re.search("^You.*Python.$", text) #^You. = string has to begin with You
                                      # *Python.$ = string has to end with Python.

if x:
    print("Yes, we have a match!")
else:
    print("No match!")
