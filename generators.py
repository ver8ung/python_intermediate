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

print(next(newGenerator)) #raises StopIteration
