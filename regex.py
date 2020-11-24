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

#regex function and metacharacters special sequences and sets
# findall matches

text2 = "Python is very very easy to understand."
x = re.findall("very", text2)

print(x)

# search for the first white space

text3 = "Hello this is a test message!"
x = re.search("\s", text3)

print(x)
print ("First white-space position:", x.start())

#search without match

text4 = "Today is Tuesday!"
x = re.search("rain", text4)
print(x) # None means no match

#split strings at each white space

text5 = "Hello and good day Sir!"
x = re.split("\s", text5)
print (x)

#controlling the number of occurences
