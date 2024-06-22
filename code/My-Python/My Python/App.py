# Printing
print("Hello World")

print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

# Variables
person_name = "Hithesh"
person_age = 77
你好 = "Ni Hao"
print(你好)
print("Hi. I am " + person_name + ". I will be " + person_age.__str__() + " next year!")

# Find Type
print(type(person_name))

# Data Types -------------------------------------------------------------------
# Text Type
my_string = "Hello World"

# Numeric Types
my_int = 20
my_float = 20.5
my_complex = 1j

# Sequence Types
my_list = ["apple", "banana", "cherry"]
my_tuple = ("apple", "banana", "cherry")
my_range = range(6)

# Mapping Type
my_dict = {"name": "John", "age": 36}

# Set Types
my_set = {"apple", "banana", "cherry"}
my_frozenset = frozenset({"apple", "banana", "cherry"})

# Boolean Type
my_bool = True

# Binary Types
my_bytes = b"Hello"
my_bytearray = bytearray(5)
my_memoryview = memoryview(bytes(5))
# ------------------------------------------------------------------------------

# u can only multiply a string by int. If u do with float its error
# Output of division is always float. But floor div is an int. 10//3 is 3 and not 3.33 - it divides n does a floor
# But output of floor division of floats is still float
# addition or multi or sub with float is always float
# -10//3 is -4. Since -3.33 floor is -4
# 10 ** 2.5
# 2.5 ** 3
# floor is the left value in number line, ceil is the right value in number line. So floor of -2.2 is -3
# floor of 2.0 is 2

# 10 % 4 = 2
# -10 % 3 = 2      :::: this is because division takes the least value until -10. Since -9 is > -10, the operation goes till -12 and then subs it.
# 10 % -3 = -2
# -10 % -3 = -(10 % 3) = -1
# 10 ** -1 = 1/10 = 0.1
# x % y --> remainder of x/y
# if x is +ve --> remainder of x/y
# if x is -ve --> y - (x % y)
# in mod div the result always has the sign of divisor

# "Ra" == "ra"    ::: False
# 3 > 3    ::: False
# 3 >= 3    ::: True
# Jupyter notebooks auto prints a variable value wihtout print statement
# bool(0) or bool(0.0) or bool("") is false
# bool(32.42) or bool(-22) or bool("hello") or bool(" ") is true

# Order of ops for operator eval - BODMAS - brackets, exponent, div, multi, add, sub
# True == 1 is True
# False == 0 is True

# 400 % 500 = 400
# 3 % 4 = 3
# 1 % 5 = 1
# 5 % 5 = 0
# 4 % 2 = 0
# 7 % 5 = 2
# 0 % 200 = 0
# 0/200 = 0.0
# 1/0 = ZeroDivisionError

# print?   ----works in Jupyter notebook
# print("hello", "world", sep= ' ', end= '\n')

# for iterator in iterable: -> doctor is iterator and patients are iterable

# range (start, end, jump) -> start is inclusive, end is exclusive
# range(10)  -> here 10 is end so its exclusive. Iterates only till 9. start is 0 and jump is 1. start + jump
# So range(10) is same as range(0, 10, 1)
# range(10, 2, -1)  10,9,8,7,6,5,4,3,2
# range takes only int
# in case of contradiction u get empty list:
# range(2, 10, -1)  since start is 2 and jump is -1: 2 - 1 = 1 but 1 is not in range 2 to 10
# range(5, 5) start is inclusive n end is exclusive
# len(range(10)) 11 items
# list(range(10))

# n * (n + 1)/2   sum of n numbers

# length of an array vs len of the count of the len of array: len(str(len(range(4321432))))

"""
Jump Statements:
pass
continue
break
"""

"""
GCD/HCF of 2 nums - greatest common divisor or Highest common factor
ex: 3 and 5 has value 1 that divides both clean. So they r co-primes. 1 is common divisor for 3 n 5.
Primes have 1 n itself as divisors. 
For co-primes GCD is always 1.
ex: 6, 8 -> 1, 2 are common factors. Highest is 2
ex: 5, 10 -> 1, 5 are common factors. Highest is 5

Range of GCD btw 5 n 10 would be [1, 5] or 1 to min factor of the higest value here 10 - min(5, 10)
"""

"""
LCM - Lowest common multiple
multiples of 2 - 2,4,6,8
multiples of 3 - 3,6,9,12
LCM(2,3) = 6 since 6 is min num that is multiple of both
LCM range starts with max num. [max(a,b), a*b]

LCM(a,b) = a * b / HCF(a,b)
"""

"""
list indexing for a list of size 5
forward or positive indexing: 0 to 4   so last inedex is (n-1)
backward or negative indexing: -5 to -1 so last inedex is (-n)
"""

# In Jupyter notebook press list. + tab to see autocomplete methods
# Use method? to see doc string. Ex: list.append?

"""
list1 + list2
list.append(elem or new_list)
list.insert(pos, elem or new_list)
list.extend(new_list)

x = list.pop(optional index: defaults to last index -1)
list.remove(elem) # removes first occurrance if dups exist

list.count(elem) # num of occurrances of elem

print(99 in list) # membership operator - checks if elem present in list

for iterator in iterable:
    do_something
    
dir(range(5)) # if u find __iter__ method then it is an iterable. dir method lists all methods of an object

sum(list) # adds all elems in list
min(list)
max(list)

avg = sum(list) / len(list)

value = int(input("Enter value: "))
"""

"""
Slicing
start index : end index : step size
list(0 index : length of list : step size 1) 
list(::) 0, len, 1
list(::-1) -1,-(len+1),-1 

l = [0,9,1]
print(l[:100]) # does not crash

l = [0,9,1,44,2,2,3,93,2,4,5,5]
l[-1:-4:-1] # [5, 5, 4]
l[2:-1] # [1, 44, 2, 2, 3, 93, 2, 4, 5] last index is -1 in negative indexing. So this is not contradiction
l[2:0] # contradiction
l[3::-1] # [44, 1, 9, 0]
l[2:8:3] # [1, 2]
Get reversed list - l[::-1]
Get even indexed elements
Get odd indexed elements
Sum of odd indexed elemnts - sum(l[1::2])
Sum of even indexed elemnts - sum(l[::2])
Sum of first 3 elems and last 3 elems - sum(l[0:3]) + sum(l[-3:])


-ve indexing gives reverse list

if step/jump is +1 then start index = 0, end index = len of list
if step/jump is -1 then start index = -1, end index = -len of list - 1

if contradiction result is empty
"""

"""
import copy
def transpose(A):
    # [1, 2, 3] [1, 4, 7]
    # [4, 5, 6] [2, 5, 8]
    # [7, 8, 9] [3, 6, 9]

    C = copy.deepcopy(A)
    for i in range(len(A)):
        for j in range(len(A[i])):
            C[j][i] = A[i][j]
    return C
    
transpose([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
"""

"""
ord(char) - get ASCII value of char
chr(ord) - get char of ASCII value

"a" * 2 = "aa"

formatted string:
f"Hello {name}"

"hit vu".capitalize() = "Hit vu"
"hit vu".title() = "Hit Vu"
"#$hit &*!vu".title() = '#$Hit &*!Vu'
"hit vu".count("H") = 0
"hit vu".count("hi") = 1
"hit vu".replace("h", "H") = "Hit vu"  # replace all occurrances
"hit vu".split() = ["hit", "vu"] # returns a list of string. default delimiter is space

" --> ".join(["hit", "vu"]) = 'hit --> vu'

list("hello") = ['h', 'e', 'l', 'l', 'o']

str(None)
str(True)
str(12.2)

"hit vu".find("u") # 5
"hit vu".find("z") # -1

"Aa".islower() # false
"Aa".isupper() # false
"a b".isalpha() # false
"a b".isalnum() # false
upper
lower

Palindrome - same forward n backward - MALAYALAM, MAAM,

Strings r immutable 
"""

"""
Get memory location of element
l = [1, 3]
m1 = id(l)
l[1] = 2
m2 = id(l)
m1 == m2
lists are mutable if u can update the element and the memory location of list remains the same
"""

"""
tuples r immutable Data struct

t = ()
type(t)  # empty tuple

t = (2)
type(t)  # integer

to use single tuple val
t = (2,)

Trap:
t = tuple("Hello") # ("H", "e", "l", "l", "o") since string is iterable
so if u need to consider as a string or a tuple with 1 elem
t = tuple("Hello",)

count - counts num of occ of elem in list
index - gets index of elem

tuples r 10x faster than lists as they r immutable

# this returns a tuple - called tuple packing
def foo():
    return 1,2,3
    
a, b, c = foo() # unpacking

tuples r heterogenous means they accpet all types 

x = (1,)
y = (2,3)
z = x + y # (1, 2, 3) this is because we r creating z and not updating. so this is allowed
"""

"""
swap values
a, b = b, a
"""

"""
Sets
{}
unordered - if u create in speicfi order the order wont be same on access. Cannot index them. they r jumbled up on storage
unique vals only

s = {}
type(s) # dict n not set

s = {1,}
type(s) # set. we cannot create empty set this way

s = set() # empty set

s = {"hello"} # {"hello"}
s = set("hello") # {"H", "e", "l", "l", "o"} this is casting

check if set is iterable
dir(set)

u can remove set items using remove and pop. pop does it randomly as no index

sets r mutable. we can add n update

del function deletes from memory. deletes any type of variable n not just set
del s

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
fruits.update(["mango", "grape"]) # this is trap. same as extend in list
print(len(fruits))

fruits.update("Hithesh") # this is trap. 

s1 = {1, 2, 3}
s2 = {2, 5, 3}
s1.intersection(s2) # {2, 3} common elems present in both sts
s1.union(s2) # {1, 2, 3, 5} all elems in both sets. unique
s1.difference(s2) # {1} present in s1 and not in s2

sets cannot be added s1 + s2
"""

"""
in - membership op
x in list
"""

"""
runs = [12,45,61,91,55,88,53,234,98]
for i in runs:
    runs.pop()
    print(i) runs

Output:
[12, 45, 61, 91] # because list is updated live it only iterates 5 times
"""

"""
Dictionaries
Keys are unique n immutable
Values can be dup

x = {} # empty curly braces is conisdered a dict n not a set

x = hash("R")

names = ["hit", "vu", "ana"]
age = [19, 11, 33, 44, 3, 2, 55]
mydict = dict(zip(names, age))
mydict # {'hit': 19, 'vu': 11, 'ana': 33} # since keys are only 3, only 3 values r considred

if u access key not present in dict u get error. 
To avoid error use --- dict.get[key, default=None]

if u have dup keys then the latest or last key and value r considered

Nested dictionaries
x = {a : 1, b : {small: 2, large: 3}}
x[a] # 1
x[1] = 5 # update
x[b][small] = 1


Append dict2 to dict1
a = {a : 1, b : 2}
b = {c : 1, d : 2}
a.update(b) # {a : 1, b : 2, c : 1, d : 2}


if u assign a new value to a key not present in dict then it appends new key value pair to the dict
x = {a : 1, b : 2}
x[c] = 3 
print(x) # {a : 1, b : 2, c : 3}

dict.items() # list of key:value pair tuples [(), ()]

for x in dict.items():
for key, value in dict.items(): # unpacking
    
len(dict) # num of key val pairs

for x in dict.keys():
for x in dict.values():

default iteration is on keys
for key in dict:
    print(key, dict[key])
    
    
Check if key exists
if key in dict:
if key in dict.keys():


def freq_dict(s):
    freq = {}
    for i in s:
    if i not in freq:
        freq[i］ = 1
    else:
        freq[i] += 1
    return freq
freq_dict ("RRR") # {'R': 3}


Delete items in dictionary
prices = {'apple': 1.50, 'banana': 0.75, 'orange': 1.25}.
del prices['banana']
prices.pop('banana')


abc = {}
abc[1] = 1
abc['1'] = 2
abc[1] = abc[1] + 1 # {1: 2, ‘1’: 2}


dict = {5: 'a', 10: 'b', 15: 'c'}
dict[0] # error
dict.get(0) # None 

"""

"""
In python everything is obj

isinstance(str, "Hello") # True

class Students:
    pass
    
s1 = Students()
type(s1)

isinstance(s1, object) # True
isinstance(s1, Students) # True

s1.name = "Hit" # is valid way of assigning attribute to obj even if it doesnt exist in class
"""

"""
Inheritance - inherits props n methods from parent class
Polymorphism - same methods exhibit diff behaviour
Encapsulation - Group code
Abstraction - hide parent attributes from children

If u want to get value of class variable use ClassName.variable instead of instanceName.variable 
u can maintain count of instances by incrementing class variable count on every init method call

Everytime an instance is created only the __init__() method gets called. So even if the class has global vars initialised to 0 they dont reset on new instance creation.

class Student:
    my_name = "Hit"
    instance_num = 0
    
    def __init__(self, name):
        self.my_name = name # instance variables or attributes
        Student.instance_num += 1 # On every new instance the count is updated

    def updateName(self, newName):
        self.my_name = newName
        

s1 = Student("Jack")
s1.my_name # Jack

s1.updateName("Jaco")
s1.my_name # Jaco

Student.my_name # Hit
"""

"""
class A:
    pass
    
if A():
    print("hello")

Above A() object exists. Hence it evals to true.
"""

"""
Under methods

def __init__(self):
def __str__(self): # print obj with custom text 
def __add__(self, other): # add 2 obj      obj1 + obj2
def __lt__(self, other): # less than <     obj1 < obj2


class A:
  def __init__(self, a):
    self.a = a
  def __add__(self, b):
    if isinstance(b, int):
      return A(self.a + b)
    return A(self.a + b.a)
  def __str__(self):
    return f"{self.a}"
one = A(1)
two = A(2)
print(one + two + 100)
"""

"""
Multi level inheritance
class A inherits class B inherits class C

Multiple inheritance
class A inherits class B, class C
"""

"""
Private attribute

self.__varName
"""

"""
Method resolution order
if same var name exists in both clases n u r trying to inherit 2 classes then left class gets priority
Class that first inherits is considered left and later one is right and the next will be left

class A:
    pass 
class B:
    pass
class C(A, B):
    pass 
class D:
    pass
class E(C, D):
    pass

x = E()
E.__mro__ # (__main__.E, __main__.C, __main__.A, __main__.B, __main__.D, object)    gives order of execuction of classes
"""

"""
l = [1,2,3,4]
def square(x):
    return x ** 2
sql = list(map(square, l))

cl = list(map(lambda x: x**3, l))

(lambda x: x**3)(pass arg)

(lambda x : x if x < 5 else 0)(4)
"""

"""
students = [
    {'name': 'A', 'marks': 50},
    {'name': 'B', 'marks': 100},
    {'name': 'C', 'marks': 40},
    {'name': 'D', 'marks': 70},
    {'name': 'E', 'marks': 60}
]
sorted_students = sorted(students, key=lambda x: x['marks']) # sort in asc by marks 
sorted_students_by_name = sorted(students, key=lambda x: x['name'], reverse=True)
"""

"""
Higher order func: a function that takes one or more functions as arguments, or returns a function as its result
def exp(x, n):
    def exp(n):
        return x ** n
    return exp(3, 6)

type(exp(3,2)) # function
"""

"""
Decorator: pass func into another func as arg
https://python-forum.io/thread-40585.html

def f1(f2):
    def f(x):
        print("-" * 20)
        f2(x)
        print("-" * 20)
    return f

######################################### way 1 

@f1
def f2(name):
    print(f"hello {name}")
    
f2("Hithesh") 

######################################### way 2 

def f2(name):
    print(f"hello {name}")
f1(f2("Hithesh"))
"""

"""
List comprehension:
l = [i ** 2 for i in list] # square each elem

map: mapp each elem in list to a func
l = map(mapping_func, iterable)

l = [1, 2, 3]
res = list(map(lambda x : x ** 2), l)) # this is faster than for each or list comprehension


For multiple lists: If lists are uneven it takes min list
A = [1,2]
B = [3,4]
result = list (map(Lambda x, y: x + y, A, B))
"""

"""
Check time taken to execute:

l = list(range(1, 100001))
%timeit [i ** 2 for i in l]
%timeit map(lambda x : x ** 2), l)
"""

"""
Filter based on logic:

l = list(filter(filter_func, iterable))
"""

"""
Zip

l1 = [1,2]
l2 =[True, False]
l3 = dict(zip(l1, l2))
l4 = list(zip(l1, l2))
"""

"""
Reduce - compress

from functools import reduce
l = [1,2,3,4,5]
l2 = reduce(lambda x, y : x + y, l) # n(n+1)/2
adds consecutive values - 1+2, 3+3, 6+4, 10+5

"""

"""
from functools import reduce
l = ["Hey,", "please", "join", "this", "sentence."]
x = reduce(lambda x, y: f"{x} {y}", l) # 'Hey, please join this sentence.'

u can do factorial with reduce
"""

"""
Arbitrary arguments
def func(a, b, *args):
    print(args) # args is tuple
    pass
func(1,2,3,4,5,6,7,8)

unpack tuple:
a, b, *c = [1,2,3,4,5,6]

Keyword arguments

arg order in function:
positional -> *args —> keyworded —> **kwargs
def random(x, y, z, *args, **kwargs):

kwargs is a dict
"""

"""
def random(x, y, z, *args, **kwargs): 
    print(f"x is -> {x}")
    print(f"y is —> {y}")
    print (f"z is —> {z}")
    print (f"args is -> {args}") print (f"kwargs is -> {kwargs}")

random (1, 2, 3)

Output:
x is -> 1
y is --> 2 
z is -> 3
args is -> () 
kwargs is -> {}
"""

"""
list.sort() # sort by lexico
sorted(list) # sort by len. preserves lexico 
"""