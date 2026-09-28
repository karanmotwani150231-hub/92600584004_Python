#1. import complete module
import mymodule2
print("addition",mymodule2.add(10 , 5))

#2.import specific function
from mymodule2 import subtract
print("subtraction",subtract(10 , 5))

#3. import module with alias
import mymodule2 as m
print("value of x", m.x)
