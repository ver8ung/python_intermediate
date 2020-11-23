# local scope of a function
# x is only stored inside testfunc and cannot be accessed outside the function
def testfunc():
    x = 200
    print(x)


testfunc()
# print(x) will return an error

# acessing local variables from a function inside a function
def newfunc():
    x = 2000
    def newfunc2():
        print(x)
    newfunc2()
newfunc()
#newfunc2 is only called inside the scope of newfunc and cannot be called outside of it

# global variables (can be accesed "everywhere")
y = 123

def global1():
    print(y)

global1()
print(y)

# naming and renaming variables (z inside function can be used differently)
z= 150

def rename():
    z = 24
    print (z)

rename()
print(z)

# global keyword makes variables global
