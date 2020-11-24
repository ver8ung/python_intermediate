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

text5 = "Hello and good day Sir !"
x = re.split("\s", text5)
print (x)

list = iter(x)

for i in list:
    print(i)

#controlling the number of occurences with maxsplit (default -1) or separator

text6 = "The weather today is cloudy."
x = re.split("\s", text6, 1)

print (x)

#replacing with the sub function, controlling number of replacements with count

text7 = "Hello what is your name?"
x= re.sub("\s", "$", text7, 1)   # 1 = 1 dollar sign (count)

print (x)

#match object

text8 = "This is a test notification!"
x = re.search("test", text8)

print(x) # shows match on position 10 - 14

# using span to search for upper case

text9 = "this is intentionally Spelled wrong."

x = re.search(r"\bS\w+", text9) # r means treated as string, \bS -> uppercase S

print(x.span())

#string property

text10 = "I am starting to run out of ideas."

x = re.search(r"\bI\w+", text10)

print(x.string)
