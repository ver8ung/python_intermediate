# using format() to format strings

#adding placeholder {}
number = 31
word = "thirty one"
newmsg = "The number is {} for you!"
print(newmsg.format(number))
print(newmsg.format(word))

#print number with 2 decimals .2f

number = 25
newmsg2 = "Your number is {:.2f}" #:=string

print(newmsg2.format(number))

#adding multiple placeholders
