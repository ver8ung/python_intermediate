# generators in python
def Items():
    print("First item!")
    yield 15

    print("Second item!")
    yield 25

    print ("Last item!")
    yield 40

newGenerator = Items()

print(next(newGenerator))
print(next(newGenerator))
print(next(newGenerator))

# print(next(newGenerator)) a 4th time creates StopIteration
# using return inside the generator function terminates it after return is called

#generator with for loop

def Upto(x):
    for i in range(x):
        yield i

seq1 = Upto(7)
while True:
    try:
        print("The number is:", next(seq1))
    except StopIteration:
        break
#print(next(seq1))


# yield square of number#
def squareSeq(x):
    for i in range(x):
        yield i * i

newGenerator2 = squareSeq(7)

while True:
    try:
        print("Recieved on the next(): ", next(newGenerator2))
    except StopIteration:
        break
