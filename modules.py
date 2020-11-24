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
import stats
