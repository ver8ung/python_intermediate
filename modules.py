# Python built-in modules (predefined functions that can be used globally, written in C)
import os # modules to interact with operating system
os.mkdir("F:\\tempdir")
os.chdir("F:\\tempdir")
os.getcwd()
os.chdir("F:\\tempdir")
x = os.getcwd()
print(x)

os.rmdir("F:\\tempdir")
os.listdir ("F:\\tempdir")

# sys module
import sys

sys.maxsize
sys.path
sys.version

#math module loads popular mathematical functions
import math

math.pi
math.e
math.radians(20)
math.degrees(math.pi/5)
math.sin(30)
math.cos(40)
math.tan(0.5)
math.log(20)
math.log10(15)
math.exp(2)
math.pow(2, 3)
math.sqrt(100)
math.ceil(5.59)
math.floor(5.59)

#statistics module
import statistics

statistics.mean ([3, 5, 7, 10])
statistics.median ([3, 5, 7, 10])
statistics.mode ([3, 5, 7, 7, 10]) #most common value

#collections and namedtuple
import collections
player = collections.namedtuple ("player", ["name", "age", "team"])
p1 = player ("Salah", 27, "Egypt")
print(p1.name)
print(p1.age)
print.(p1.team)

#collections and ordered dict
dict1 = collections.orderedDict()
dict1["First:"] = 35
dict1["Second:"] = 40
dict1["Third:"] = 45
dict1["Fourth:"] = 50
for k,v in dict.items(): # k=key v=value
           print(k,v)
    
#deque function
dq = collections.deque ([20, 25, 30, 35])
dq.appendleft(15)
dq.appendright(40)
q.pop()
q.popleft
q.popright

#random module pseudo-random number generator function
import random as rd

rd.random()
rd.randint(1,50)
rd.randrange (1, 10)
rd.randrange (1, 10, 2)
rd.choice ("Python)
rd.choice ([1, 2, 3, 4, 5])
