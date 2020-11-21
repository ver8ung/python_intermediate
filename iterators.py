# Iterators
# iterate over items in tuple
testtuple = ("banana", "lemon", "apple")
testiterator = iter(testtuple)

print(next(testiterator))
print(next(testiterator))
print(next(testiterator))

#iterate over sequence of characters
teststring = "lemon"
testiterator2 = iter(teststring)

print(next(testiterator2))
print(next(testiterator2))
print(next(testiterator2))
print(next(testiterator2))
print(next(testiterator2))

#looping over a tuple
testtuple2 = ("banana", "lemon", "apple")

for i in testtuple2:
    print(i)

#looping over a string
teststring2 = "banana"

for i in teststring2:
    print(i)
