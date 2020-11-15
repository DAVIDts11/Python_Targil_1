#!/usr/bin/env python
# coding: utf-8

# # Functions

# A function is a block of organized, reusable code. Functions provide better modularity for your application and a high degree of code reusing. In addition, they also make your code more readable, as they keep the main code simple by assigning tasks to auxiliary funtions. 
# 
# We've seen some of Python's built-in functions like *int()*, *print()*, *type()*, etc., and object functions such as those belonging to **string**s. We will now learn how to create user-defined functions.
# 
# A function receives input arguments and **returns** some output based on them. Both the input and the output can in general contain zero arguments, for example the function _print()_ returns no argument and the _bit\_length()_ function if **int** receives no input. 
# 
# Every function definition starts with a *signature*, containing the prefix **def** followed by the name of the function and parentheses, in which the input arguments are listed. Then, following a colon and an indentation, the function block is written, possibly containing a **return** statement(s). As python is dynamically typed, there is not declaration of return type for functions.

# In[ ]:


def add(a,b):
    total = a + b
    return total
print (add(12,-9))


# In[ ]:


def strToBool(s):
    test = s.lower()
    if test == "false" or test == "f":
        return False
    elif s.lower() == "true" or test == "t":
        return True
    return None
print(strToBool("FAlsE"))
print(strToBool("true"))
print(strToBool("t"))
print(strToBool("F"))

print(strToBool("Maybe"))


# **None** is the Python equivalent of **null**. The comparison is not one to one, as Python's **None** is an object in its own right, however the use is similar.

# In[ ]:


print(type(None))
print(bool(None))
print(strToBool("fa") is None)


# In Python, a function can return multiple values for a single function call. When calling such a function, we can accept all returned values into one variable, which will hold a Python **tuple** object. Alternatively, we can **unpack** the returned values accross multiple variables, each holding one value. For the latter option, we must know how many values are returned.

# In[ ]:


def calculate(a,b):
    c1= a+b 
    c2= a-b 
    c3= a*b
    c4= 0 if b == 0 else a/b
    return c1, c2, c3, c4
tup = calculate(80,15)
v1,v2,v3,v4 = calculate(10,0)
#p1,p2 = calculate(11,12) #error
print("tuple: ", tup)
print("values: ",v1,v2,v3,v4)


# **Functions can define default values for input parameters. All non-default params must come before default params.**

# In[ ]:


def prints(s,caps=False):
    s_ = str(s)
    toPrint = s_.upper() if caps else s_
    print(toPrint)

prints("This sentence is printed as is.")
prints("this one is all caps",True)
prints(True,True)
prints(False,True)


# **Function input parameters are assigned in the order they are sent, however they can be explicitely defined in the function call**

# In[ ]:


implicit=calculate(2,4)
explicit=calculate(b=2,a=4)
print("implicit:",implicit)
print("explicit:",explicit)


# In[ ]:


def poly(a,b=1,c=1,d=0):
    return str(a)+"x^3 + " + str(b) + "x^2 + " + str(c) + "x + " + str(d)  

print("1:",poly(2))
print("2:",poly(2,3))
print("3:",poly(2,3,4))
print("4:",poly(2, d=9))
print("5:",poly(10,11,d=17))
##print("6:",poly()) #error - at least 1 param required
##print("7:",poly(2, b=8, 15)) #error - can't have positional argument after keyword
##print("8:",poly(2, 7, b=12)) #error - b received multiple values: positional + keyword


# What if we want to expand the above _polynomial_ function so that we can have more coeffiecents and degrees? Python uses the <font color="red">**\*args**</font> input parameter for variable length input. The input will be stored in a **tuple** object. We can *iterate* over this **tuple** using the <font color="blue">**for**</font> statement. 

# In[ ]:


def polynom(*coefficients):
    res=[]
    p = len(coefficients) - 1 
    for c in coefficients:
        if type(c) in (int, float): #check if the type of c is s number
            if c != 0:
                if p!= 0 and p!=1:
                    term = "{}x^{}".format(c,p)
                elif p == 1:
                    term = str(c)+"x"
                else:
                    term = str(c)
                res.append(term)
        p-=1
    return " + ".join(res)
    


# In[ ]:


polynom(5,4,3,2,1)


# In[ ]:


polynom(5.5,4.4,3.3,2e-4,1)


# In[ ]:


polynom(0,13,0,37,0)


# In[ ]:


polynom(17, "6", "100", 90, "hello", 80, (13,14,15), 0, 0, 7 )


# Logical errors can occur at runtime, these are called **Exceptions**. Python let's you catch and handle exceptions using the **try/except** statement:<br>
# try:<br>
# &emsp;\< unsafe_code \><br>
# except \< exception_type_1 \>:<br>
# &emsp;\< handle_exception \>:<br>
# except \< (exception_type_1, exception_type_3) \>:<br>
# &emsp;\< handle_exception \>:<br>
# except:<br>
# &emsp;\< handle_other_exceptiosn \><br>
# else:<br>
# &emsp;\< handle_no_exceptions \><br>
# finally:<br>
# &emsp;\< cleanup \><br>
# <br>
# *Note: **else** and **finally** are optional. The **else** block is executed only if no exception was caught, the **finally** block is always executed*.

# In[ ]:


"Exception"[100]


# In[ ]:


x = "Exception"
try:
    print(x[100])
except Exception as e:
    print(type(e))
else:
    print(x)
finally:
    print(len(x))


# In[ ]:


def castNumber(param):
    try:
        fNum = float(param)
        nNum = int(fNum)
        
    except:
        return None
    else:
        return nNum if nNum == fNum else fNum
    


# In[ ]:


print(castNumber(1))
print(castNumber(2.0))
print(castNumber(3.3))
print(castNumber("4"))
print(castNumber("4.4"))
print(castNumber("5e5"))
print(castNumber("6 "))
print(castNumber("seven"))
print(castNumber((8,)))


# In[ ]:


def polynomial(*coefficients):
    """
    Returns a string representing a polynomial expression with given coefficients.
    With 'n' being the length of the input, the (i)th element in the tuple will
    belong to the (n-i-1)th degree.
    Arguments:
    *coefficents - arbitrary length sequence of numeric or string representation of numeric values.
    Returns:
    string - representation of polynomial
    """
    res=[]
    for p,c in enumerate(reversed(coefficients)):
        c_ = castNumber(c)
        if c_ is not None: #check if the type of c is s number
            if c != 0:
                if p!= 0 and p!=1:
                    term = "{}x^{}".format(c_,p)
                elif p == 1:
                    term = str(c_)+"x"
                else:
                    term = str(c_)
                res.append(term)
    res.reverse()
    return " + ".join(res)
    


# In[ ]:


help(polynomial)


# In[ ]:


polynomial(17, "6", "100", 90, "hello", 80, (13,14,15), 0, 0, 7 )


# # Classes

# Python is an object oriented language, which uses classes as object templates. Classes are defined using the `class` keyword.
# Object instances are created by calling the class constructor method: `classInstance = className()`<br>
# In python, there is not distinction between private/protected/public class variables. This means you can manually modify the internals of an object throught the program life cycle. Care must be taken so as not to damage the inner workings of a class.

# In[ ]:


class Dummy:
    x = "dummy"
    
    def printMe(self):
        print(self.x)


# In[ ]:


d=Dummy()
d.printMe()


# In[ ]:


Dummy.x


# In[ ]:


d.x=99
d.printMe()


# In[ ]:


Dummy.x


# In[ ]:


def printMe():
    print("hello world")
d.printMe = printMe
d.printMe()


# *Note: you can override a function inside an instance of a class, but you cannot bind it to the instance's "self" parameter.*

# In[ ]:


d1 = Dummy()
d1.printMe()


# In[ ]:


def printMore(self):
    print(self.printMe)
Dummy.printMore = printMore


# In[ ]:


d2 = Dummy()
print("d2:")
d2.printMe()
d2.printMore()


# In[ ]:


print("d1:")
d1.printMe()
d1.printMore()


# **Modifying the Class itself affects all previously created instances as well**

# In[ ]:


Dummy.x = "Another dummy"
print("d2:")
d2.printMe()
print("d1:")
d1.printMe()


# In[ ]:


d1.x = 100
Dummy.x = "Yet another dummy"
print("d2:")
d2.printMe()
print("d1:")
d1.printMe()


# *Once an instance variable has been overriden, it is no longer bound to the class variable.*

# ### The class __init__() function
# The `__init__()` function is one of Python's magic (dunder - double underscode) functions. There are functions that are implicitly called when performing specific actions in Python. The `__init__()` function is called when creating a new class instance (i.e. calling the class constructor). By default, any class functions, including `__init__()` accept the **self** parameter as their first argument. This must be explicitly defined in the function declaration.<br>
# We use the `__init__()` function to initialize new instances.

# In[ ]:


class Vector:
    import math
    """
    Vector class defining a 3-dimensional Vector object with coordinates x,y,z.
    """
    x,y,z = (0,0,0)
    
    def __init__(self,x=0,y=0,z=0):
        if type(x) in (int,float):
            self.x = x
        if type(y) in (int,float):
            self.y = y
        if type(z) in (int,float):
            self.z = z
    
    def multiply(self,m):
        """
        Multiply vector by a given scalar value.
        """
        if type(m) in (float,int):
            self.x *= m
            self.y *= m
            self.z *= m
    
    def length(self):
        return self.math.sqrt(self.x**2 + self.y**2 + self.z**2)


# In[ ]:


v = Vector(2, 4, 4)


# In[ ]:


v.multiply(3)
print(v)
print(v.x,v.y,v.z)


# In[ ]:


print(v.length())
print(v)
print(v.x,v.y,v.z)


# In[ ]:


def VectorString(self):
    """
    String representation of a Vector object.
    """
    return "({},{},{})".format(self.x,self.y,self.z)
Vector.__str__ = VectorString


# In[ ]:


print(v)


# *The `__str__()` function of a class is called when the string representation of an instance is required.*

# In[ ]:


def VectorAdd(self,other):
    res = Vector()
    if type(other) == Vector:
        res.x = self.x + other.x
        res.y = self.y + other.y
        res.z = self.z + other.z
    elif type(other) in (int,float):
        res.x = self.x + other
        res.y = self.y + other
        res.z = self.z + other
    else:
        res = str(self) +" "+ str(other)
    return res
Vector.__add__ = VectorAdd


# In[ ]:


print("v:",v)
v1 = Vector(100,100)
print ("v1:",v1)
print ("v+v1:", v+v1)
print("v:",v)
print ("v1:",v1)


# In[ ]:


print("v1+5:",v1 + 5)
print('v1+"is a vector":',v1 + "is a vector")
print('v1+True:',v1 + True)


# In[ ]:


#print(5+v1)
#print("This is a vector:"+v1)
#print(True+v1)


# In[ ]:


def VectorAccess(self,item):
    res=None
    vec = (self.x,self.y,self.z)
    vecD = {"x":self.x, "y":self.y, "z":self.z}
    if type(item)== int and -3 <= item < 3:
        res= vec[item]
    elif type(item) == str and item in tuple("xyz"):
        res= vecD[item]
    return res

Vector.__getitem__ = VectorAccess

        


# In[ ]:


print(v)
print(v[1])
print(v[8])
print(v[-3])
print(v[-7])
print(v["xy"])
print(v["y"])
print(v["z"])
print(v[False])


# In[ ]:


v1[2] = 100


# ### Short hop back to Iterables and iteration
# We remember that there are some objects such as **strings** and **lists** that we can iterate over using `for` loops. We can also manually iterate over these object thanks to their `__iter__()` and `__next__()` functions. The `__iter__()` function returns an iterator object that implements the `__next__()` function, which allows iteration.

# In[ ]:


magicList = [1,1,2,3,5,8,13,21,34,55,89]
iterator = iter(magicList)
print(iterator)


# In[ ]:


print(next(iterator))


# In[ ]:


print(next(iterator))


# In[ ]:


print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# In[ ]:


print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# *Note: when the iterator runs out of values, the **StopIteration** Exception is raised.*

# ### We can make our class iterable by implementing the magic function `__iter__()`

# In[ ]:


def VectorIter(self):
    iterableVector = (self.x,self.y,self.z)
    return iter(iterableVector)
Vector.__iter__ = VectorIter


# In[ ]:


print(v)
for i in v:
    print(i)


# *In the above example, we do not create our own interable object, but rely on the tuple object's iteratation functionality*

# In[ ]:


v2 = Vector(1,2,3)
v3 = Vector(1,2,3)
print("Is v2 equal to v3?",v2 == v3)
print("Is v2 equal to v2?",v2 == v2)


# In[ ]:


def VectorEquals(self,other):
    if type(other) != Vector:
        return False
    for i,c in enumerate(self):
        if c != other[i]:
            return False
    return True
Vector.__eq__ = VectorEquals


# In[ ]:


print("Is v2 equal to v3?",v2 == v3)
print("Is v2 equal to v2?",v2 == v2)


# In[ ]:


v4 = (3,2,1)
print("Is v2 equal to v4?",v2 == v4)


# In[ ]:




