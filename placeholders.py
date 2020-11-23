# using format() to format strings

#adding placeholder {}
number = 31
word = "thirty one"
newmsg = "The number is {} for you!"
print(newmsg.format(number))
print(newmsg.format(word))

#print number with 2 decimals .2f

number = 25
newmsg2 = "Your number is {:.2f}" #:=after string

print(newmsg2.format(number))

#adding multiple placeholders
quantity = 5
itemNumber = 50
price = 24
firstorder = "We want {} pieces of item number {} for {:.2f} Euros."

print(firstorder.format(quantity, itemNumber, price))

#using index numbers

quantity = 7 # = index number 0
itemNumber = 77
price = 23.55
secondorder = "We want {0} pieces of item number {1} for {2:.2f} Euros."
print(secondorder.format(quantity, itemNumber, price))

age = 30
name = "Thomas"
newmsg3 = "The name is {1}. {1} is {0} years old."
print(newmsg3.format(age, name))
