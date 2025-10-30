# String data type

# literal assigment
first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constractor function
pizza = str("Peperroni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

#concatination
fullname = first + " " + last
fullname += "!"
print(fullname)

#Casting a number to a string
deacde = str(1989)
print(type(deacde))
print(deacde)

statement = "I was born in " + deacde + ".s"
print(statement)

#Multipleline
mline = """ 
Hey how are yoy?

I was just checking in.
                                                All good?
"""
print(mline)

# Escaping special char
sentence = 'I\'m back at work\tHey!\n\nWhere\' this at\\located?'
print(sentence)

#string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(mline.title())
print(mline.replace("yoy", "!!!"))

print(len(mline))
mline += "      "
mline = "      " + mline
print(len(mline))

print(len(mline.strip()))
print(len(mline.lstrip()))
print(len(mline.rstrip()))

# build a menu
title = "menu".upper()
print(title.center(20, "="))
print("coffee".ljust(16, ".") + "$1".rjust(4))
print("Mafen".ljust(16, ".") + "$2".rjust(4))
print("Chesecake".ljust(16, ".") + "$4".rjust(4))

#string index values
print(first[1])
print(first[-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

# Boolean datd type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float type
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

#complex type
comp = 5+3j
print(type(comp))
print(comp.real)
print(comp.imag)

# built in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# CASTING STRING TO A NUMBER
zipcode = "10001"
zip_val = str(zipcode)
print(type(zip_val))