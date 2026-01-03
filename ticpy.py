# x = [1,2,3]
# y = x
# y[1] = 4
# print(x)#output:[1, 4, 3]
# ========= dunder functions ==========
class Person:
        def __init__(self,name):
                self.name = name
#__init__ runs automaticaly when you create an object
b = Person("moichel")
print(b.name)
# __init__ constructor
#called when an object is created
class Number:
        def __init__(self,x):
                self.x=x
                
        def __add__(self,other):
                self.other = other
                return self.x + self.x
c = Number(3+5)       
print(c)
# __getitem__
# __it__,__gt__ 
#__eq__
#__call__
#dunder functions allow
#operator overloading(+,==,<)
#custom behavior for built-in functions
#cleaner and more pythonic code
"""
__init__ object creation
__str__ user-friendly print
__repr__ debugging
__len__ len()
__add__ +
__eq__ ==
__getitem__ indexing
__call__ callable object"""




# You said:
# what is this function
# ChatGPT said:
# Which function are you looking at? 🙂
# Paste the function (or a screenshot of the code), 
# and tell me what language it’s in if you know it
# —I’ll break it down line by line.

# You said:
# __repr__ python
# ChatGPT said:
# Ah, __repr__ — a classic Python “dunder” (double-underscore) 
# method 🐍

# What __repr__ is
# __repr__ defines the official string representation of an object.

# Python calls it when:

# You type the object in the interpreter

# You use repr(obj)

# The object appears inside a container (list, dict, etc.)

# Simple idea
# __repr__ answers: “How should this object look to a developer?”

# Example
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"Person(name={self.name!r}, age={self.age})"
# p = Person("Mike", 25)
# print(p)
# Output:

# Person(name='Mike', age=25)
# Without __repr__
# You’d get something ugly like:

# <__main__.Person object at 0x7f8c2a3b>
# __repr__ vs __str__
# Method	Purpose	Used by
# __repr__	Developer-friendly, precise	repr(), interpreter
# __str__	User-friendly, pretty	str(), print()
# If __str__ is not defined, Python falls back to __repr__.

# Best practice
# __repr__ should return a string

# Ideally, it should be unambiguous

# Bonus points if it could recreate the object:

# Person(name='Mike', age=25)
# Quick rule of thumb
# Debugging → __repr__

# Displaying to users → __str__





 