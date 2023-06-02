# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 08:13:49 2023

@author: George.Harpum

Explanation of python concepts
Contents (Line number, title)
58 Built-ins
80 Try block
96 Numbers
101 Operators
137 Strings and Comments
173 String Operators
182 Variables
197 In place assignment operators
210 Types
219 Type hinting
231 Conditionals
252 If statements
301 Some keywords
360 Loops
392 Data Structures
440 Indexes
473 Packing
490 Slicing
620 Nesting
656 Iterables
774 Comprehensions
882 Functions and methods
909 Parameters
926 Returning
958 nth length parameters
1060 Type checking
1102 Wrappers
1237 Class things
1334 attribute vs method
1381 Inheritance
1508 Multilevel inheritance
1526 Properties
1672 Dataclasses
1737 Built in methods
1785 Importing
1831 Chaining
1920 Some other notes
"""

print("The very basics")
# Code runs line by line.
print(1) # happens first
print(2) # happens second
# some words do things (keywords and builtins)
# print outputs to the console. 
# print is a useful builtin function that displays its input in the console.
print("Like this")


print("\n!Built-ins")
assert True
# assert is a useful keyword that errors if False, but continues if true.
# This is useful doing debugging of larger operations, to test each point and find where it doesn't match your expectation.
# WHY MIKE SHOULD CARE: add a bunch of asserts during function tests to see where it's failing


try:
    pass
    # < block of code to run >
    # stops at the line that produces an error
except: # <Exception: Optional>:
    pass
    # < block of code to run if the "try" block fails >
    # If the code in try errors, except gets run
    # can be left blank to catch any error, or a specific error can be mentioned. 

# try is a useful keyword for error handling 
# When something goes catestrophically wrong, it produces an error. 
# The error stops all other code from running.
# try and except allow you to handle the error without stopping the code.

print("\n!Try block")
try:
    assert False
except AssertionError:
    print("assert False should have stopped the code, but it didn't!")

print("see!")
# WHY MIKE SHOULD CARE: 1) code continuation while testing, 2) make a function that would otherwise error in certain situations
try:
    open("stupid butts file") # if file is an input, the input could be wrong
    # only way to prevent code erroring on a bad input is a try block. 
except FileNotFoundError:
    print("Oh dear, we can't find that file")

# There are lots of keywords and builtins functions. They will not all be covered here.

print("\n!Numbers")

1 # integer
1.0 # float

print("\n!Operators")

print(1+1) # expression gets evaluated before printing. Outputs 2
1 + 2 # spaces are not enforced but recommended for clarity
2 - 3
4 * 5
2 / 4
"+ - * /" # all work as expected
# x / y returns a float
# x // y returns an integer (floor division, the fractional part is just removed i.e., it does not round)
print(9 / 5) # 1.8
print(9 // 5) # 1
"%" # this is uncommon so I'll mention it separately
# % is the modulus operator
# The modulo is the reminder of a / b. so 5 % 2 is 1.
# this can be thought of as altering the numerical base
# counting up 5 % 2 would be 1 0 1 0 1 
# counting 5 % 3 would be 1 2 0 1 2
# (The "base" number becomes 0, so base 2 is 0 and 1)
# This makes sense when you think we don't have a character for 10.
# We have the numbers 0 to 9 and 10 is saying we have now wrapped to the beginning
# The number of times we've wrapped is denoted by a second unit. 

assert 5 % 3 == 2
# this is said "5 Mod 3"
# this can be very useful in computing

# ** can be used for indices.
print(2**8)

# floats can be used in indices
print(9**0.5) # x^(a/b) = (b(th)root(x))**a so x^(1/2) = square root of x ** 1 == sqrt(x)
# In words: X to the power A over B is the B root of X to the power of A. 
# I'm not removing this just live with it Mike. 
# Fractional powers can be important

print("\n!Strings and Comments")
# This is a comment
# Python ignores comments
"This is a string" # Comments can go after code and the code runs normally
""" This is a string across
multiple
lines
"""

"" # string
'' # string
" '' " # string in string
' "" ' # string in string
# If you want the sentence: It's a tough life
print("It's a tough life") # use different string characters.
# in other languages '' is for single characters 'a', 'b'; and "" is for "strings like this"
# Python doesn't hold you to that so whatever boats your goat
formated = "fancy"
print(f"This is a {formated} string") # formatted, or "f" strings allow for in place evaluation
# inside an f string, the {} can be used to denote a variable name that 
# Formatted strings allow for some very useful text formatting.
print(f"This is a percentage {0.1234:.1%}") # : denotes the formating of what's in the {}
# .1 means to 1 decimal place, % means as a percentage. 
# 0.1234 as a % is 12.34% to 1dc, that's 12.3%
# There's other stuff like padding (adding filler characters) 
# Continue to explore this on your own.

# Special characters can be called with '\'
print("Newline\nTab\tTab") # \n is a new line. \t is a tab (there are more, left to the reader as an excerise for themselves)
print(r"this is a literal string \n") # r'' denotes a literal representation of the string
# it ignores special characters

print('It\'s possible to \'escape\' special-characters so they\'re treated literally') 
print("\\") # escaping an escape key


print("\n!String Operators")

# + and * have string implementations

print("Hello" + "World") # + concatenates strings (adds them together raw)

print("Hello" * 5) # * duplicates the string n times


print("\n!Variables")

x = 0 # this is a variable
# Variables assigned with '='

a, b = 1, 2 # variables can be assigned in line
# This is only recommended if your variables are related (for readibility)
print("a:", a) # outputs 1
print("b:", b) # outputs 2

print("x:", x) # out 0
x = 1 # Variables can be overwritten
print("x:", x) # out 1


print("\n!In place assignment operators")

a = 1

a += 2 # a = a + 2
assert a == 3
a *= 3 # a = a * 3
assert a == 9
a -= 4 # a = a - 4
assert a == 5
a /= 5 # a = a / 5
assert a == 1

print("\n!Types")
# everything in python has a type
# here are 4 basic types
int
float
str
bool


print("\n!Type hinting")
# python is "Dynamically typed" which means it works out what everything should be for you
# so you can type 1.0 and it knows to make it a float.
# However, sometimes things get confusing so it's nice to tell humans what things should be
# enter, type hinting.
# this uses a ':' BEFORE assignment with the type
x: int = 1
# however, this doesn't actually _do_ anything
x: float = "str" # <- this would throw an error in a statically typed language. but again, it's a hint, not a law.
# WHY MIKE SHOULD CARE: It's useful for yourself and others to know what should go where
# more use cases will be mentioned later

print("\n!Conditionals")

True # Boolean (named after George Boole)
False # Boolean
# only two values, true or false.

# Conditional statements that EVALUATE to a boolean
# 2 inputs, 1 boolean output
1 > 2 # False
2 == 4 # False (== means is this equal, as = is variable assignment)
0 < 5 # True
1 != 3 # True (does not equal)

# also <=, >= (less/greater than or equal), arrow must come first

assert True # recall: continues with True, errors with False
1 < 2 # Evaluates to True
assert 1 < 2 #  continues because "assert True" continues
# in python True and False must have a capitalised


print("\n!If statements")

if True: # must have a ':' and an indent
    # do
    pass # placeholder keyword to remove SyntaxError (if must be followed by an indent)
elif False: # else - if. Presents another conditional that is only checked if the first fails
    pass 
else: # runs if the conditional was false, not mandatory
    pass

# Code runs in order
if True:
    print(1)
elif True:
    print(2)
else:
    print(3)

# Only 1 gets printed because its the FIRST true statement
if True:
    print(1)

if True:
    print(2)
else:
    print(3)

# 1 and 2 printed as second statement is pure if (a separate statement) not "else if" 
x = 1
y = 2
# WHY MIKE SHOULD CARE: if you don't get why if statements might be useful there's no hope for you
# Ordering your if statements properly is very important because the first true statement is run. 

# If you want to print the largest number
print("The biggest number:")
if x > y: # if x > y. you know x is the larger number
    print(x) # print the largest number
else:
    print(y) # if x > y false then either Y is bigger or Y is the same. Either way, you can print y

# if you want to do something different when x == y, then elif is your friend
if x > y:
    print("Big boy X")
elif x == y:
    print("Same")
else:
    print("Big boy Y")


print("\n!Some keywords")


"or"

# or returns true if the first OR the second statement is true
# for speed, or checks the first, if true, it skips the second statement 
# (because it doesn't matter if it's true or false after the first is true)

if x < y or x == y:
    print("Less than or equal to")

"and"
# returns true if both statements are true
# for speed, skips second if first is false
x, y, z = 1, 1, 1
if x == y and y == z:
    print("All the same")
# WHY MIKE SHOULD CARE: allows to chain conditions together in one block
# and make more specific conditions

"cleaner conditional"
# This was just a cool example I found
# if you have a set of values which would want to accept.
# you might do something like this for n = 2 values
# allow only the two values
if x == 1 or x == 2:
    pass # do something
# or, you might want to make the error case instead
# The error case tends to be better practice inside functions (mentioned later)
# for clarity: Instead of allowing specific values, you prevent all the other values
# It's "better practice" inside a function just because it looks cleaner, I don't think it's faster.
if x != 1 and x != 2: # if x isn't 1 and x isn't 2, then error
    raise ValueError("value not accepted") # raise causes an error to happen
# However, this can be rewritten as
if x not in (1, 2): # this is better practice
    raise ValueError("only accepts x=1 or x=2")
# this also works for more acceptable values
if x not in (1, 2, 3, 4):
    raise ValueError("only accepts values of (1,2,3,4)")

"not"
not x # returns the opposite bool value
not True # False
not False # True
# also includes sensible syntax

l = []
x not in l # this better practice
not x in l
# technically "not in" is a diferent keyword than the strung together "not" and "in"
# this is just for readibility.
"in"
# on it's own 'in' is a membership test
# x in y returns True if the element x is present in an iterable y.
# iterables are explained later.
# WHY MIKE SHOULD CARE: as above, testing membership allows (or disallows) certain values


print("\n!Loops")

while True: # this would run forever as statement cannot change
    # do
    pass
    break # keyword for stopping a loop (very useful)
    # after code runs, checks the condition again, if still true, it does it again
    continue # keyword for skipping the rest of this loop (rechecks the conditional and goes again)
    # continue doesn't do anything here because if it was before break then the loop never ends

i = 0
while i < 5: # expression that is reevaluated each loop when i = 5, i < 5 is False and loop stops
    print("again", i)
    i += 1 # increases 1 once per loop

"else"
# while loops also have an else keyword
# as a while loop is testing a condition, if that condition is ever false the loop stops
# if that condition is false - you can add an else keyword to have some additional code
i = 0
while i < 3:
    i+= 1
    if i == 5:
        break
else:
    print("This loop ended naturally")
# the else allows you to have a block of code that runs when the while loop ends because of its condition
# if the if statement did break the loop - the else block WOULD NOT RUN

# WHY MIKE SHOULD CARE: loops are very important in a wide range of applications.
# the else keyword is less common but can be invaluable when needed. 

print("\n!Data Structures")
[] # this is a list
() # this is a tuple
{} # this is a dictionary
{1,} # this is a set -- only defined empty with set() 

# can also be defined as
list()
tuple()
dict()
set() 
# each accept an 'iterable' and makes that their contents (more on this later)
# dict is a special case because it requires a pair of inputs (key and value) will be discussed later
list([1, 2, 3]) # same as [1, 2, 3]
# however it becomes useful with variables
t = (1, 2, 3)
l = list(t)
s = set(t)
# list and tuple, [] and (), are ordered (have an index)

# things with {} are unordered (they have no numerical index)
# As of python 3.7 dictionaries are actually ordered. so... soz.



["this", "is", "a", "list"] # generally for homogenous data (this is a soft recommendation)
("this", "is", "a", "tuple") # generally for heterogenous data
{0: "this", 1: "is", 2: "a", 3: "dictionary"} # for unique pairs (the key must be unique, the value needn't be) (keys of 0-n is just a list in disguise)
{"this", "is", "a", "set"} # for *unordered* unique items (does not allow replicates)

{"a", "this", "set", "is"} # same as above (printing a set has no guarantee the order it will appear in)

# lists, sets, and dictionarys are mutable (change be changed)
# tuples are immutable (cannot be changed after definition)

# you can do reassignments to get around this but the original object is immutable

# WHY MIKE SHOULD CARE: data structures are absolutely vital to programming
# lists: generally the easiest to use for any instance of "I need multiple things in one variable"
# Tuple: immutable, useful when you want to prevent change. Also use less memory
# Dictionary: having custom keys to things can be extremely helpful
# sets: fast checking membership is great
# Examples
# list: a list of names
# tuple: a list of options at program start that won't change
# dictionary: dict of names to ages
# sets: set of sites a product is manufactured in.

print("\n!Indexes")
# An index is the order of data in a data structure. 
# For tuples and lists, indexes start at 0, and increment in ones 
['a', 'b', 'c'] 
# 'a' is at index 0
# 'b' is at index 1
# 'c' is at index 2
[1, 2, 3]
# the same applies (e.g. 1 is at index 0)

# In dictionaries, they do have have a separate index becuase they are indexed by their keys
{0: 'a', 1: 'b', 2: 'c'} # the same as the above list (in terms of index)
# The differences will be the ways in which they can be manipulated, because one is a list, the other a dictionary. 
# But dictionaries allow for non-numeric keys (indexes)
{'a': 0, 'b': 1, 'c': 2} # the keys have been reversed, now 0 is at index 'a'
# The index terminology is not often used with dictionaries, as they are keys
{0: 'a', 15: 'b', -365: 'c'} # This is why it's not an 'index' because it follows none of the conventions.
# Although dictionaries are ordered behind the scenes (this was actually introdued in python 3.7)
# Dictionaries have no real need to be. 
# The fact that 'b' comes after 'a' is essentially meaningless if you access the items by keys.
# Having the order is useful in terms of perserving order in other structures e.g. list(dict)
# And also it improves memory use and iteration performance (according to the internet)
# Anyway
# Sets don't have an index
# Sets are unordered collections, 
s = set(t) # from above
try:
    s[0]
except TypeError:
    print("Sets are not 'subscriptable', you cannot attempt to slice them because they have nothing to slice with")
    
# WHY MIKE SHOULD CARE: understanding indexes is essential to working with Data structures   

print("\n!Packing")
a = 1, 2, 3 # a is a tuple
# same as a = (1, 2, 3)

# can be reversed
a, b, c = (1, 2, 3)
# also works with lists, sets, and dicts
# Dictionaries also default to keys
a, b = {1: 'a', 2: 'b'} 
assert a == 1
assert b == 2

# WHY MIKE SHOULD CARE: very useful tool to working with data structures
# python tends to do some tuple packing in the backend for some stuff
# e.g. when doing functions (mentioned later) "return a, b" will return a tuple of (a, b)
# This is mentioned later

print("\n!Slicing")

# For items with indexes, the value at the index position can be called with a "Slice"
" slice operator is <variable>[start:stop:step] "
# Buckle up boy'o
l = [1, 2, 3]
assert l[0] == 1 # indexes start at 0 (this is vital to remember, get this tatoo'd on your body)
assert l[0:2] == [1, 2] # wait a second... 0 1 2, that's three items, why did it only show 2?
# slicing is stop EXCLUSIVE (it doesn't include the item at the stop position)
assert l[0:3] == [1, 2, 3]
# using extremes in the slice can be made implicit rather than explicit. 
# this is done by leaving the item blank
assert l[1:] == [2, 3]
assert l[:] == [1, 2, 3]
# unless the step is being changed '::' is the same as ':'
assert l[::] == [1, 2, 3]
assert l[::2] == [1, 3] # stepping 2 rather than 1
# a list can be reversed with a negative step
assert l[::-1] == [3, 2, 1]
# the last item of the list is also at index -1
assert l[-1] == 3 # as an integer, this will be useful later
assert l[-1:] == [3] #as a list

# WHY MIKE SHOULD CARE
# Knowing indexes and how to use them (slices) is one of the most important skills of a beginning programmer
# some specific examples
s = "8strip"
s2 = "16strip"
# I want the number out
assert s[0] == '8'
assert s2[0] == '1'# I want both digits 
assert s2[0:2] == '16' 
# but that requires two different slices.
# If I have input x and I want to know which strip it is, how do I know to get 8 and 16
# note that the strings are different lengths
# you could
def strip_num(x):
    if len(x) == 6:
        return s[0]
    else:
        return s[:2] # recall that [0:x] and [:x] are the same
# but that doesn't seem the best.
# note that  "strip" is always 5 characters long, regardless of the start.
assert s[:-5] == '8'
assert s2[:-5] == '16'
# see how much easier that was. 
# [:-x] says from the start up to the index of -5.
# negative indexes start at -1 from the last element and decrease until the start
# '8' 's' 't' 'r' 'i' 'p'
#  0   1   2   3   4   5
# -6  -5  -4  -3  -2  -1
# Another way to think about it is if you double up the string
# The first character will be the 0 of the number line. 
# '8' 's' 't' 'r' 'i' 'p' '8' 's' 't' 'r' 'i' 'p'
# -6  -5  -4  -3  -2  -1   0   1   2   3   4   5
# this means that the first character is also the negative length of the string.

assert s[-(len(s))] == '8'
# the last character is the length - 1
assert s[len(s)-1] == 'p'

# All the above applies to tuples also
t = (1, 2, 3)
# also applies to tuples
assert t[0] == 1 
assert t[0:2] == (1, 2)
assert t[0:3] == (1, 2, 3)
assert t[1:] == (2, 3)
assert t[:] == (1, 2, 3)
assert t[::2] == (1, 3)
assert t[::-1] == (3, 2, 1)

l = [1, 2, 3]
# however, lists can do slice assignment
l[0] = 3 # make the 0th item 3
assert l == [3, 2, 3]
# Tuples, being immutable, cannot.
try:
    t[0] = 1
except TypeError:
    print("Tuples are immutable")

# dictionaries are "sliced" using keys, not indexes
d = {
    1: 'a',
    2: 'b',
    3: 'c'
}

assert d[2] == "b"
# however, can't use a non-existent key
try:
    d['c']
except:
    print("d['c']")
    print("The Key 'c' doesn't exist, the keys are [1, 2, 3]")

# They have no numerical index either
try:
    d[0]
except:
    print("d[0]")
    print("Dictionaries are not indexed")

# You can still do assignment, however
d[1] = 'b'
assert list(d.values()) == ['b', 'b', 'c'] # note that "a" == 'c' ("" and '' are still strings)

# you can also assign to a non-existant key
d[4] = 'c'
assert d[4] == 'c'

# WHY MIKE SHOULD CARE: A real example
# I made a character counter using this concent
string = "The quick brown fox jumped over the lazy dog" # your string
dist = {} # a currently empty dictionary that will be filled with letter distribution
for letter in string: # looping over each character - explained momentarily
    try: 
        dist[letter] += 1 # try and increment the letter by 1
    except KeyError: # if the key doesn't exist, it will throw a key error
        dist[letter] = 1 # if key doesn't exist, make it
print("distribution of letters", dict(sorted(dist.items(), key=lambda item: item[1], reverse=True)))
# sorted() sorts an iterable as a list
# dict turns it back into a dictionary
# dict.items() returns a list of tuples of (key, value)
# key is what item to sort by
# we're telling it to use the second (index 1) item of the tuple to sort by
# reverse is saying do it backwards (largest first)
# at some point I'll explain lambda but as of 09.05.2023 I don't

print("\n!Nesting")

# a list of tuples
l = [(1, 2), (2, 3)]
assert l[1] == (2, 3)
# chained slicing
assert l[0][1] == 2 # first item of list is (1, 2), 2nd item (INDEXES START AT 0) of (1, 2) is 2

# This can go n deep for funsies.
# WHY MIKE SHOULD CARE: real example
# base-python implementation of tables
table = {
    'a': {0: 0, 1: 1, 2: 2, 3: 3},
    'b': {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
     }
# This is the table
# index |  0    1    2    3
# -------------------------
#  'a'  |  0    1    2    3
#  'b'  | 'a'  'b'  'c'  'd'
# Stored as a two dictionaries
# row 'a'
print(list(table['a'].values()))
# row 'b'
print(list(table['b'].values()))

# columns name
print(list(table['a']))
# column 2 (3rd column)
for col in table.values(): # mentioned next
    print(col[2])
# or
print([col[2] for col in table.values()]) # mentioned later
# this could be properly implemented as a functions or a class
# However it will be slower than Pandas so it's generally easier to use that.

print("\n!Iterables")
# an iterable is something that can be iterated over
# interations is the process of examining every element
# you can iterate over datas structures, as they have multiple elements

print("For")
l = [1, 2, 3, 4, 5]
for x in l: # variable is assigned each item of the iterable in turn. doesn't need to be pre-defined before the loop
    print(x) # first loop, x = 1, 2nd loop, x=2 etc
# alternatively - each loop is incrementing a hidden variable (lets call it h)
# for x in y, each loop (starting at 0) h is incremented by 1.
# in each loop (before any of your written code) x = y[h]
# so first loop, h=0 (a hidden count). then (behind the scenes) x = y[0]
# in the case of "for x in l", the first loop -> l[0] = 1 so x = 1 it should be 0?
l = [1 ,2, 3]
assert l[0] == 1 # first item
y = 0 
assert l[y] == 1 # y = 0, l[0] = 1
for butts in "Hello": # strings are made up of characters, so they are also iterable
    print(butts) # variable can be called anything

# WHY MIKE SHOULD CARE: There are examples throughout this file that use for loops as a part of it.
# looping is so important it's included in basically every programming language
# fun fake "HASKELL" doesn't have loops, but it does have recursion and that's kinda similar.

"else"
# as while loops, for loops also have an else keyword.
# it works in the same way,
# if the for loop finishes naturally (looping for each element and then terminating)
# then the else block runs
# just as an FYI, even though both are loops, I saved "for" for now because of the data structures.

print("Generators")
# a generator is a lazy-iterator
# If you wanted a list of 1_000_000 items, having a list of a million items stored in memory is quiet large
# However, if you only want to do something to each element, and then be finished with it, you can use a generator
range(10) # this is a generator
# it produces the numbers in the range from either (stop) or (start, stop) 
# if you give it one parameter it treats it as the stop number
# this generates the numbers 0 to 9 (stop exclusive)
# There are also iterators which, depending what you're doing, are just worse generators.
# Defining an iterator is a class object with 2 dunder methods (mentioned later) while a cusomter generator is easier
# I'll describe a custom generator later in the function section

l = []
for x in range(10):
    l.append(x) # adds item x to the list "l"
print(l) # the main reason I'm doing append is to save lines on the console when running this massive file

# during the loop x isn't stored in memory. it's overwritten with a new value.
# We're then taking this x value and storing it in memory (in a list)
# Range is theoretically infinite because of this, with little performance decrease due to the size of the range.
# obviously printing 1_000_000 numbers will take longer than printing 10
l = []
for x in range(1_000_000_000_000, 1_000_000_000_010):
    l.append(x - 1_000_000_000_000)
print(l)
# despite big numbers, still low memory, takes the same amount of time

for x in range(3):
    print("let's go again")
# this is the same as
i = 0
while i < 3:
    print("wee")
    i+=1
# but takes fewer lines
# WHY MIKE SHOULD CARE: I won't show the code here because it'll just be confusing 
# When going multiple expensive operations it will be better to do them one at a time
# an example is making a graph.
# In my own code I want to make lots of graphs from an excel sheet.
# In some instances I make hundreds of them
# Graphs take _a lot_ of memory.
# Therefore, in my script it was much better to write my own generator
# this makes a graph, does everything with it (labels, and etc) and then saves it.
# the graph is then removed from memory (which is fine because it's saved to disk) 
# and then it makes the next one. 
# This basically allowed my code to work because making 200 graphs in memory at once was way too much
# pyplot produces a warning if you make more than 20

print("Enumerate")
# This is a very handy builtin
"for x, y in enumerate(iterable)"
# x is the index enumerate returns (a counter that increments by one each loop)
# y is the element of the iterable

# I'll compare to a while loop
i = 0
while i < 1:
    print("i is the counter of the number of while loops")
    i += 1
# i is the 'index' / counter of loops the while loop has done. 
# you can do the same with conventional for loops
i = 0
for x in [1,2,3,4]:
    print(f"{i} loop returns {x}")
    i += 1

# enumerate is literally just this in built-in
for index, elem in enumerate([1, 2, 4, 8, 16, 32, 64]): # powers of 2
    print(f"{elem} is the {index} power of 2")

# another example
for idx, letter in enumerate("Hello World"): # strings are iterables
    if letter == "l":
        print("there is an 'L' at position", idx)

# you technically don't have to do idx, elem and can just do x
for x in enumerate("abc"):
    print(x)
# but you'll see that this is actually a tuple containing the running index and the item
# enumerate also takes a start parameters
for x in enumerate("abc", start=1):
    print(x)
# this just allows you to change what the index starts at.
# this is very useful.


print("\n!Comprehensions")
# This is going to get a bit more difficult, so bare with.

# One line if:
1 if True else 0
# This is a valid if statement
# Other languages have a special character for this, called the ternary operator
# in python, it's just a single-line version of an if statement.
"value_if_true if <condition> else value_if_false"
# simple as.


# I'll mention now:
# Python likes chaining simple things together to make them more complex.
# Later, I'll mention method chaining, but for now, that if statement is pretty understandable
# you have to know the order, of course, but then, it's quite simple to read
x = 1
y = 2
a = 1 if x < y else 0 
# a is going to be 1 if the condition is met, else, it'll be 0
print(a)

# Single line for:
# These can't be done just anywhere so I'll now define Comprehensions

# A comprehension is an easy (one-line) way of making a data structure using iterations
# The most common is a List Comprehension 

l = [x for x in l] # this actually makes the same list over again
"<result> for <item> in <iterable>"
# lets look at the second half first
# for <item> in <iterable>
# this is the same as a normal for loop
# however - a normal loop would then expand onto the next line
# the next line says - "what do I do with each item of x?"
# to answer that question on a single line we have 2 options.
# 1) put it after
# 2) put it before
# python goes with option 2.
# you can do whatever you want with each item (that fits in a single line)

# heres an example using a generator (range is a generator)
# recall that range provides start -> stop (with each step)
# range(10) provides 0 -> 9 (stop exclusive) adding 1 each time (default options)
l = [x for x in range(10)]
print("list comp:", l)
# read this as "x", "for x in range(10")
# not as "x for x", "in range(10)"
# x, on it's own, is saying just give me each item in the iterator.

# this is the same as
l = []
for x in range(10):
    l.append(x)
# but that's three lines! 
l = [x+1 for x in l] # makes the same list but everything is +1
# more examples, by printing the list rather than storing it in a variable
print([2*x for x in range(1, 6)])  
print([x**2 for x in range(1,11)])
print([x/2 for x in range(10)])
print([1 for x in range(5)]) # this ignores x, giving you 5 1's
# best practice for a loop that doesn't use the looping variable is '_'
print([1 for _ in range(5)]) # '_' will still equal each item of the loop
# it's just good convention to tell others that the variable isn't used in the loop


# We can chain for and if together
l = [x for x in range(10) if x % 2 == 0] # The for-if statement does not allow an "else" (it automatically excludes)
# recall that x % 2 is testing reminder of division.
# where x % 2 == 0, x is divisible by 2
print(l) # these are the even numbers

"x for x" # this is also a little boring
# lets do something fun
l = [x.upper() for x in "hello"]

# strings can be iterated over 
# x is the character of each string (which in python is a str object)
# strings have methods that can be called on them (using the '.')
# .upper() on a string returns the uppercase version of that string.
print(l) # now uppercase (upper can be called on the whole string, but if for some reason you wanted a list of characters)
# this is actually the same as 
print(list("hello".upper())) # but I hope my point comes across

# this can be stringed together to do many functions onto each x.
ord # this is comprehension that gives the ordinance (the ascii numerical representation) of a character
l = [ord(x.upper()) for x in "hello"]
print(l)
# WHY MIKE SHOULD CARE: comprehensions are incredibly powerful 
# they replace multi-line for loops and conditionals into a single line
# I most commonly use comprehensions with if statements in practice. 
l = [1,2,3,4,5] # I do still write out low size lists
l = [x for x in range(1, 6)] 
# or
l = [x+1 for x in range(5)] # to get around the 0 start and n-1 stop
# but a list of 100 integers long
l = [x for x in range(100)]
# or even worse for characters
l = ['a', 'b', 'c'] # I have to write the 3 characters for each item (the char and the quotes)
# however
l = [x for x in "abc"] # nicer
l = [x for x in "abcdefghijklmnopqrstuvwxyz"] # much nicer
# you can also
l = [chr(x) for x in range(97, 97+26)]
# chr converts an integer into it's ascii character
# the lower case letters start at '97 = 'a' and will obviously end 26 letters later


print("\n!Functions and methods")

# Basically the same thing, just used in different contexts

# Functions are pre-writting blocks of code that exectute when called at a later time
# WHY MIKE SHOULD CARE: It saves on how much code you have to write
"defining"
"""
def function_name(paramaters):
    # do stuff
    <return> optional
"""

def print_nums(num: int) -> None:
    i = 0
    while i < num:
        print(i)
        i += 1
    # Notice that num here is a placeholder variable. It hasn't been defined yet, but it isn't producing an error
# This doesn't do anything
print("\nPrinting Numbers Now")
print_nums(5) # this prints the numbers
# also note, whatever gets passed gets treated as "num" in the function, but doesn't actually have to be named num

butts = 1
print_nums(butts) # works just the same

print("\n!Parameters")
# Parameters are the things going in, also called arguments

def default(x=1, y=2): # convention says to have no space between x=1
    return x, y # returned as tuple
# the x and y paramters have default paramters
print("default:", default())
print("custom:", default(4, 5))
# Note, positional arguments must come before keyword arguments (any argument that is default value")
"""
try:
    default(x = 1, 2)
except:
    print("Doesn't work")
"""
# this is a language syntax problem so "try" doesn't actually get around it, annoyingly. 

print("\n!Returning")
# Functions can return variables

def add_one(x: int) -> int:
    x += 1
    return x
# same as
def add_two(x: int) -> int:
    return x + 2 # it computes this expression before returning the value

print("\nNow doing functions")
number = 3
add_one(number)
print("Hold on a second")
print("Where's my number?")
# add_one is returning by it has nothing to give it to. 

num_2 = add_one(number) # assigns the returned value to variable
print(f"First number {number}\nSecond Number {num_2}")

# a function that doesn't return actually returns None
a = print()
assert a == None
# Print does stuff, sure (it outputs to console) but it doesn't give anything back

def func():
    return
    return None
    
    # all of those are the same (including the blank line)
    # return None is generally best practice

print("\n!nth length parameters")

def average(x, y, z):
    return (x + y + z) / 3
# this works great
# But what if I want custom lengths?
print("*args")
#What I want to do is:
def average_list(nums: list):
    return sum(nums) / len(nums) # built-ins for total sum and total length of an iterable 

l = [1,2,3,4]
print("average_list: ", average_list(l))
# but now I have to make a list of my numbers

def mean(*args): # *args allows any length of comma separate positional arguments. 
    return sum(args) / len(args)
# args is a common convention but it can be anything, it's recommended to name it something readable
assert mean(1, 2, 3) == 2


def keywords(**kwargs): # ** says to make a dictionary of any nth length keyword arguments
    for x in kwargs:
        print(x, kwargs[x])
    
keywords(x=1, b=2, c=3) # can input whatever you like

def do(*nums, **kwargs) -> float:
    if kwargs.get("mode", None) == "avg":
        return sum(nums) / len(nums)
    return sum(nums) # this only runs when the if statement is false
# the if statement True returns a value - the function stops when it returns
# if it didn't return the average, any other action is being directed to return 'sum'


# dict.get(x, y) returns the value associated with the key 'x'
# if key 'x' doesn't exist, it returns y. 
# this isn't the most elegant way handle this but  it gets the point across
# y defaults to None but I included it here to explain it

print("do avg:", do(1, 2, 3, mode="avg"))
print("do sum:", do(1, 2, 3, mode="sum"))
print("do anything:", do(1, 2, 3, mode="hnseuifhj ifsw", butts=14, eleven=11))

"A return to Generators"
# Generators are like functions, except instead of "return" they have "yield"
def gen(*args):
    x = len(args) # do different things based on number of arguments provided
    if x == 1: # just one argument is the "stop"
        start = 0 # default start
        end = args[0] # end value
        step = 1 # default step
    elif x == 2: # len two - start, stop
        start = args[0]
        end = args[1]
        step = 1 # default
    elif x == 3: # len 3, start, stop, step
        start = args[0]
        end = args[1]
        step = args[2]
    else:
        raise TypeError(f"gen expects 1-3 positional arguments but {x} were given")
    start = 0
    while start < end:
        yield start # the yield keyword makes it a generator
        # this gives back the variable "start" during each yield of the generator. 
        start += step
# This is a python implementation of the builtin 'range'
# Custom functions will ~almost~ always be slower than builtins. 
# Built-ins use C, you're using python. C will beat python every time.
# why not use default paramters?
# this is why
def range_(start=0, stop=0, step=1):
    while start < stop:
        yield start
        start+=step
# this is short and looks great
range_(1) # but what does this do?
# this replaces the default "start", not the stop
range_(start=1) # you have to do this every time
range_(0, 1) # or this
# The above 'gen' is meant to replicate the custom positional argument implementation
# range works normally by something called "function overloading"
# this is where a DIFFERENT function is called based on what is inputted
# e.g. if 1 value is given, call the range(stop) version
# if 2 values are given, call range(start, stop), etc.
# I'm too tired to dig into function overloading inside python, as I've never done it before
# if you want to play around with overloading, do it one your own laddy


"type hinting in functions"
# This is a very useful case for type hinting
# look at add_one again. Type hinting tells you that it takes a int and returns and int. 
# good to know
# (again, python doesn't care)
def twice(x: int) -> int:
    return x + x

twice(2) # returns 4
twice("str") # returns "strstr" because of str concatenation (2*x would do the same thing)


print("\n!Type checking")

# This can be protected against
def itwice(x: int) -> int:
    if isinstance(x, int): # returns true if type of x is an int
        return x + x
    else:
        raise TypeError("itwice only accepts integers")
# WHY MIKE SHOULD CARE: doing the wrong things with functions is sometimes too easy. 
# it also helps if you're working with abstracted data in some way.
"isinstance(obj, type)"
# returns True is obj is type, else returns false
# this is the same as
"type(obj) == type" 
# but isinstance is better practice (and faster)

"raise"
# this raises an error of a given error type.
"TypeError(message)" # (it actually takes *args but in simple terms)
# this will raise a TypeError (the error to raise when a function is passed the wrong type)
# There are many builtin expections and you can even make your own, these will be mentioned later.

try:
    itwice("str")
except TypeError:
    print("Now we stopped it from working with strings")


print("\nFunctions as objects")
# Everything in python is an object
# This means
butts = itwice
print(butts(1))
# Without the () the itwice is the function OBJECT (it's not being called)
# butts is then being made the function object, so it can also be called to the same effect. 

# calling the below methods prints out all the methods and attributes of the class
# This will make more sense after learning about classes
str.__dict__ # Includes normal methods (mentioned later) and Double-underscore (Dunder) methods (special python things)
dir(str) # does basically the same thing (if __dir__ not defined returns the attributes)

# So what can we do with this ability?
print("\n!Wrappers")
# We can "Wrap" a function in another


def do(func): # takes a function as input (because functions are objects)
    def wrapper(): # defines function inside a function
        print("Before")
        
        func() # calls the inputted function
        # note that this function takes no arguments and returns no value
        print("After")
        
    return wrapper # returns the wrapper as an object


def f(): 
    print("I do stuff")

f = do(f) # lets go step by step
# here f, defined as the function <print("I do stuff")>
# > do takes a function (in this case f)
# > do then defines (but does not execute) a function called wrapper
# > as part of wrapper, it calls the specific function passed to do()
# > do then returns the OBJECT of the wrapper function that has just been defined

# before the above line. "f" on it's own is the object of the function defined above
# now, f is the object of the wrapper function (that has f called with it)
# calling f now
f()
# is basically the same as wrapper()
# however, this wrapper is specific to the function passed into "do"

def g():
    print("I do something else")

g = do(g)
# this is the same, but the wrapper calls g() not f()
g() 

print("See how before and after are the same, but the function itself is different")

# This is the simplest execution of this idea

# WHY MIKE SHOULD CARE: this is complicated but can be very useful
# the simplest example is timing functions (shown below)
"A real example"
from time import perf_counter # performance counter, an accurate way to record time
from functools import wraps # a helper decorator (not mandatory but useful to have)
# I'll explain imports later

def timethis(func): # takes function in (same as "do" above)
    @wraps(func) # this just makes it clear to python that this is a wrapper for the function (func)
    # this isn't mandatory but it helps remove some small annoyances to do with function namespaces (advanced)
    def timing(*args, **kwargs): # define wrapper, but notice now with arguments and keywords (any possible length)
        start = perf_counter() # precise time when called
        
        out = func(*args, **kwargs) # record the output of the function, now with all of its parameters
        
        result = perf_counter() - start # calculate the time that has passed since the first timing
        print(func.__name__, result) # print the function's name and how long it took to run
        
        return out # return the value from the func
    return timing # returns the wrapper as an object

@timethis # saves having to write mean = timethis(mean) - literally all it does
def mean(*args):
    return sum(args) / len(args)

# if we now call
print("result: ", mean(1,2,3,4,5)) # notice it includes the time

# I hope you can understand what the *args and **kwargs are doing. 
# timing takes in any possible arguments and passes them to the function without (in this instance) touching them
# the same for the keywords. 
# they also don't have to be only *args

@timethis 
def add(x, y):
    return x + y

print(add(1, 2)) # this will now error if more arguments are passed into it
# even though add is actually the wrapper "timing" (which accepts any length of arguments)
# Add (inside the wrapper) still only accepts two, and thus will error

# you "could" make the wrapper function a limited number of parameters
# but it makes it more specific so it depends what the wrapper is doing .

def intify(func):
    @wraps(func)
    def makeint(*args, **kwargs):
        args = [int(x) for x in args] # recall list comprehension
        out = func(*args, **kwargs)
        return out
    return makeint

# so this is a wrapper that makes the inputs integers before they're passed into the function
@intify
def sums(*args):
    return sum(args)

# normally strings of numbers cannot be treated as numbers,
try:
    sum([1, 2, '3', '4'])
except TypeError:
    print("Input must be all numbers (int/float)")
# well now they can
print("sums result: ", sums(1, 2, '3', '4'))

# although that wrapper may be error prone because it has no protection for what goes into int()
# int obviously cannot convert a number not in base ten.
try:
    int('a')
except ValueError:
    print("Int needs to have decimal number as string")
# Although, in the case of "mean", trying to sum things that aren't numbers would error anyway.

# WHY MIKE SHOULD CARE: Think of it like this
# if functions are a way of generalising a piece of code to work with different inputs
# a wrapper is a generalised piece of code to work with different functions
# A wrapper is a functions function, in a way.
# you can time any function (above)
# modify the input (above)
# create a logging file (not shown)



"Methods"
# So what are methods then?

# Methods are functions attached to a class
# "But what's a class?"
# A class is a custom object
# What's an object?
# Basically everything in python is an object.
# 1 is an object, "this is an object", ("so", "is", "this")
print("\n!Class things")

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


# Lets go slowly through this.
# A class is a standard block of code that can be uniquely assigned to an instance.
# (what's an instance)
# It's basically a variable

a = Person("Tom", 27)
b = Person("George", 22)
assert a != b
# While both a and b are of type person, they contain different "instances" of the class
assert isinstance(a, Person) # note that a type is basically a class without being called (it doesn't have brackets)
int('1') # converts str to int
int # type 
list # type
list((1, 2,  3)) # converts tuple to list
# neat huh
# WHY MIKE SHOULD CARE: Classes can be used to generalise code that has needs different instances
# If you only want one person throughout your code a class may not be the way to go
# There is also a school of thought for 'functional' programming which doesn't involve classes
# It's not fully clear what they mean in some cases because C and Rust doesn't have classes
# but they have 'structs' which act an awful lot like classes and I have no idea why they're different

"__init__"

# So what's this boy then?

# __init__ gets called when an instance is being _init_ialised 
# this is what happens when you put the brackets around something

"self"
# as with everything python, it's not a hard rule
# However, IDEs (development environments) with syntax colouring will also colour 'self', it's that important

# but what is it?
# self is the parameter that holds the instance information.
# a != b because their self variables don't contain the same information

# the first argument of __init__ is ALWAYS the self variable
# the following parameters can be whatever you like

"self.x = x"
# This is a very common thing to do with all __init__ functions.
# you take some input variable (like name) and then you assign it to an attribute of self
# the '.' says this is an attribute of the class

assert a.name == "Tom"
assert a.name != b.name

"Methods (but I actually explain them this time)"

# A method is a function inside a class

class number:
    def __init__(self, x: int):
       self.num = x # don't need the same name
    
    def add_one(self) -> int :
        return self.num + 1
    
    def add_x(self, x: int) -> int:
        return self.num + x

x = number(1)
print(x.add_one()) # If it's not clear, the expression gets evaluated before print so print will print the return value of a statement.
# hold on, why no paramters?

"self, again" 
# in a method, the first parameter passed is always self, because different instances of "number" need to have different results
# self is passed into the method behind the scenes. 

print(x.add_x(10)) # self gets passed behind the scenes, but add_x still needs a parameter 'x'


"attributes"
# name of Person is an instance variable, an attribute.
assert a.name == "Tom"

# what's a class attribute?

class circle:
    Pi = 3.14159 # Belongs to the class
    def __init__(self, r: float):
        self.radius = r # belongs to the instance
    
    def area(self):
        return circle.Pi*(self.radius**2) # Pi belongs to class, can be called off the class or off of self
        # cirlce.Pi == self.Pi WHEN AN INSTANCE EXISTS
        # as long as the class exists so too will circle.Pi. in the above instance Pi is can also be used with self so it doesn't matter
        

print("\n!attribute vs method")
# simply, method has ()
# it means it can be called
try:
    a.name()
except:
    print("name cannot be called")

c = circle(2)
print(c.area) # this is a method without being called


"Class and Static methods"
# You can have class methods
# these are attached to the class as well as the instance

class number:
    def __init__(self, x: int):
        self.num = x
    
    @classmethod # @ (pronouced 'decorator') used to change how function is treated, in this instance passes 'cls' instead of 'self'
    def comp(cls, x) -> bool: # cls used as the class variable
        return isinstance(x, complex)
    # class.method() works for a classmethod because the cls instance is passed instead of "self" (which doesn't exist)
    
    @staticmethod # changes function to no longer be passed 'self' or 'cls' at all (frees up the first argument)
    def biggest(x, y) -> int: # nothing passed as first argument
        if x > y:
            return x
        else:
            return y

number.comp(15) # the method is called on the class
x = number(4) # made an instance as normal
x.comp # can still be called on the instance
# but as cls is passed not self, comp doesn't have any instance information
x.comp(x.num) # to test itself this would need to be done
number.comp(x.num) # same as this
# This is a poor example but I was just struggling to think of something that could be a class variable

"Static" 
# Isn't attached to either the class or the instance
print(number.biggest(3, 4)) # returns 4
# It literally is just a function
# Static method is used when you have a function that could be grouped into the class for neatness


print("\n!Inheritance")

# Classes can inherit properties from another class
# this is to save writing the same code again and again
# also keeps things organised

# Lets look at person again

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
# Now I want a class for an employee of a company
"""
class Employee:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary
"""
# hmm... there seems to be a lot of similarity there
# how about

class Employee(Person):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age) # pass this back to the "super" (parent) definition of __init__
        self.pay = salary

# With the same __init__ in the parent you don't even need to write it again!
class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f"{self.name} says {self.sound}")
    

class Dog(Animal):
    sound = "Woof"
    def Bark(self):
        print(f"{self.name} says Woof")


class Cat(Animal):
    sound = "Meow"
    def Meow(self):
        print(f"{self.name} says Meow")

# Notice that speak and bark/meow are the same, because of the class attributes
# Dog.sound and self.sound (of a dog instance) are the same thing

# So both bark and meow could be removed
# meaning only Animal had to be made, and then make a Dog with class attribute of "woof"

"Inheritance and Exceptions"

# you can also inherit from builtin classes

class integer(int):
    pass

# theoretically there are use cases of these, but I typically only see online people trying to pull shenanigans with this

# However, exceptions are the exceptions to this rule.

def sqrt(num: int, root: int = 2) -> float:
    if num < 0 and root % 2 == 0:
        raise ValueError("Even Root of a negative number not implemented")
    return x**(1/root)

try:
    sqrt(-2)
except ValueError:
    print("Look how I used a custom error")

# When making your own projects, you may encounter a situation where the builtin exceptions (the errors) are lacking
# TypeError and ValueError are useful, and common, but what if you want to error that isn't classified.
# MAKE YOUR OWWWWN

# Convention says to have Camel case (LooksLikeThis) with it ending it Error
# In one of my scripts I have

class PlateTypeError(Exception): # dervies from Exception class
    def __init__(self, plate):
        self.message = f'Unsupported Plate type: {plate}'
        super(PlateTypeError, self).__init__(self.message)   

# this allows me to 
def plateType(x, plate):
    if plate != 384 or plate != 1536:
        raise PlateTypeError(plate)

try:
    plateType(1, plate=96)
except PlateTypeError:
    print("Would return a custom error (hopefully more specific to the problem at hand)")
    
"Multiple and Multilevel inheritance"
# Multiple inheritance is where one class is derived from several super classes

class Man:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def human_things(self):
        return "Humany Woomany"
    

class Bat:
    def bat_things(self):
        return "flap flap"


class BatMan(Man, Bat): # inherits from TWO classes (gasp)
    def batman_things(self):
        return "I am the night"
    
b = BatMan("Bruce Wayne", 41)
print(b.human_things(), b.bat_things(), b.batman_things())
# See how BatMan has all the methods of Man and Bat


# Multilevel inheritance, where a class is derived from a class that is itself dervied

print("\n!Multilevel inheritance")
class A:
    def a(self):
        return "from A"
    
class B(A):
    def b(self):
        return "from B"

class C(B):
    def c(self):
        return "from C"

abc = C() # () because it's being called, but nothing because __init__ isn't defined
# C contains all functions of its parents / ancestors
print(abc.a(), abc.b(), abc.c()) # () because all functions


print("\n!Properties")

# so you've encounted attributes (class.x) and methods (class.x()) what about properties!
# A property is the horrid (but useful) offspring of an attribute and a method

class Example:
    def __init__(self, num):
        self.num = num 

    
    @property 
    def num(self):
        return self._num # leading _ means the variable is "private"
        # privacy is worthless in python
        # calling class._num from top-level is completely valid
        # It's just one of those conventions 
    @num.setter
    def num(self, num):
        self._num = num
        
# so what's this about?

# A property allows for finer control on an attribute
# A clear example would be limiting a possible value of num

# This is done via a SETTER and a GETTER
# a setter will set your value
# a getter gets your value
# both of these are functions that mediate access to an attribute

# Notice that both functions are called the same thing - normally this would be a problem
# The second function/method overwriting the first. 
# However, the first is a the getter property (using @property)
# The second function is the setter - designated with <property>.setter (notice the name)

# Now
print("Property exmaples")
e = Example(5)
print(e.num) # no need for ()
e.num = 14
print(e.num)
# isn't this convenient

# "But what's the point!" you ask
# As the setter and getter are functions, their capabilities can be expanded

# Using a common and useful example
class Celsius:
    def __init__(self, temp):
        self.temp = temp
    
    @property
    def temp(self):
        return self._temperature # this value must be called something other than temp
    
    @temp.setter 
    def temp(self, x):
        if x < -272.15:
            raise ValueError("Temperature cannot be lower than -272.15℃")
        else:
            self._temperature = x
    
t = Celsius(25)
try:
    t = Celsius(-300)
except ValueError:
    print("The setter has additional functionality!")

# Note well, the setter is also called during the __init__ function because "temp" is being set

# As mentioned above, the @ is a way to simplify some annoying code

class Fahranheit:
    def __init__(self, temp):
        self.temp = temp # not that this is not the ._temp 
        # temp != _temp 
        # This is the property and the private attribute respectively
        # Having temp here is what allows for the __init__ setting
        # Without it, it wouldn't perform the set check as _temp is just a normal attribute
    
    def set_temperature(self, x):
        if x < 10:
            print("oh no")
        self._temp = x
    
    def get_temperature(self):
        return self._temp

    temp = property(get_temperature, set_temperature)
    # just as @timethis replaced func = timethis(func)
    # @property replaces the above line
    # However, you then have to specify the setter, but it does make the code cleaner
    # @temp.setter is also just
    # temp = property().setter(temp) in disguise

# Also, not implementing a setting makes a property read only

class shush:
    def __init__(self, x):
        self._private = x
    
    @property
    def val(self):
        return self._private
    # notice that we don't include self.val in the __init__ because there isn't a way to set a value to .val
    # if we tried to set self.val = x we would get an error
s = shush(1)
print(s.val)
try:
    s.val = 4
except AttributeError:
    print(".val attribute cannot be set")

# You can also do this
s.butts = 3
print(s.butts)
# this is just a normal attribute
print(s.val)
# but you still cannot set s.val
# Also, you can't delete val

# properties have a setter, getter, and a deleter

del s.butts # keyword to delete some object

try:
    s.butts
except AttributeError:
    print(".butts no longer exists")

try:
    del s.val
except AttributeError:
    print(".val cannot be deleted as deleter not set")

# including below inside the class makes the del keyword work
"""
    @val.deleter
    def val(self):
        del self._private
"""
# notice that the property is fueled by another variable
# including self.val anywhere in the setter, getter, or deleter causes a significant fault (a kernel crash not a code error)
# this because things get self-referential in a damaging matter


print("\n!Dataclasses")

# so those animals above don't really do much. They really just hold data.
# (name, age)

# if you have a lot of classes made just to hold data, it can become tedious to write self. x = x, self.y = y, etc

from dataclasses import dataclass # I'll explain this in a bit

@dataclass # here's another decorator (that I just imported)
class Data:
    name: str
    age: int
    job_title: str
    salary: int
    commute_mins: float

# this then makes not only the __init__ but several other Dunder (double underscore) methods as well
# Some examples include __repr__ which is the __repr_esentation of the class (as a string),
# __eq__, __eq_uality for testing whether the contents of a == b (rather the instance),
# and other comparison (!=, >, >=, ==, etc)

"__repr__"
print(Data("George", 22, "Apprentice", "Not Enough", "Too long"))

"__eq__"
a = Person("Tom", 27)
b = Person("Tom", 27)
assert a != b
# hold on! but they're the same... right?
# a and b are different instances of the same class (with the same information)
# however 
a.name = "George"
assert b.name == "Tom" 
# changing a didn't also change b
# not the same instance

#  __eq__ can be used written to test the contents of the other class match their contents

class example:
    def __init__(self, x):
        self.x = x
    
    def __eq__(self, other):
        if self.x == other.x: # note this will throw an error if the "other" doesn't have an attribute called 'x'
            return True
        else:
            return False
        # Above is the long implementation
        # Alternatively 
        return self.x == other.x # this will return true if equal and false if not, exact same.

e1 = example(1)
e2 = example(1)
assert e1 == e2 # this now works because we've defined the __eq__ method.
# but that would be a lot of work to write ourselves each time (for something simple like, compare each attribute directly)
# Also, we haven't implemented > < <= or >= 
d1 = Data(1, 2, 3, 4, 5)
d2 = Data(1, 2, 3, 4, 5)
assert d1 == d2 # the contents are the same
d1.name = 5
assert d1 != d2 # contents no longer the same

# Dataclasses do a lot more as well but I won't go into that (also because I don't utilise them to their full extent yet)

print("\n!Built in methods")

# I mentioned earlier 
"hello".upper()
# you should now know what this is

# upper is a method for the class str.
# There are many methods for different data structures

# I'll demonstrate several but I advise you to learn more on your own (there are simply to many)
# Recall that a method without the brackets is actually the function object being outputted
# I'm just doing this so I don't have to provide peramaters
# Anyway, inbuilt methods:
str.upper # all upper
str.lower # all lower
str.replace # (old, new, count) replaces old str with new str, count number of times
"aw".replace('a', 'e')
"hello world".replace("l", "w", 2)
str.split # (sep, count) splits the string the sep character, count times (counting from the left) returns a list
assert "hello world".split() == ["hello", "world"] # default sep = ' ' (a space)
# I'll also point out here that
"hi".upper        () # is just as legitimate as 
"hi".upper() # however, 
"if you don't do func() you'll be taken out back and shot"
list.append # this function adds an item to a list
l = [1]
l.append(2) # this is an in-place function. I.e., it returns None but it still does something (recall print)
assert l == [1, 2]
d = {'a': 1, 'b': 2, 'c': 3}
dict.items # this returns a dict_obj list of tuples (this needs to be put into a proper data structure to do things like slices)
print("items in d:", list(d.items())) # like this 
dict.keys # dict_obj of keys
dict.values # dict_obj of values

# these work
1 in d.keys()
for x in d.keys():
    print(x)
# this doesn't
try:
    d.keys()[0]
except TypeError:
    print("dict_keys type has less functionality than a true data structure")





print("\n!Importing")
# So I promised to explain
"from time import perf_counter"
"from dataclasses import dataclass"
import time # this import the module time
# what's a module?
# a module is a collection of prewritten code so you don't have to do all the work
# some modules (like numpy) don't just use raw python, but also includes C behind the scenes
# for most things, using a module will be better than writing the code yourself.

# time is the module name
# if you want to use a function you must specific
# module_name.func_name
time.time() # time has a function called time!
time.perf_counter() # this looks familiar!

# "from" allows the importing of only specific functions
"from time import perf_counter" # this imports the function (object) 
# now it can be called only with
perf_counter() # isn't that nice
# "from" still loads the entire module, so it doesn't particularly save time, but it does reduce clutter

import numpy as np # this may actually error for you Tom. 
# if it does, go into cmdline and type: pip install numpy
# pip is python's package manager. 
# time is a module that comes with python so you can just import straight up

# numpy num-py numeric-python
# numpy is very good for doing maths operations _very_ quickly
# "as" allows us to rename the module into anything for convenience

np.array([1, 2, 3]) # some common modules have short-hand conventions
# pandas as pd, numpy as np (both for maths and data science)
# although you could do something else, e.g. pandas as p - but why bother.

# <from module import *> allows you to import every function (so you don't have to write the module name)
# This is not recommended because it can cause naming issues (if you've made a function that has the same name as the module one)

# Because python likes chaining methods
np.array([1, 2, 3]).mean().is_integer() # (this calculates the mean and then returns true if the value is an integer)
# np is saying "from the numpy module"
# array is a top-level class being initiated with the list [1, 2, 3]
# mean() is a method that returns a np.float64 (a C-based float type for numpy performance)
# The second method (is_integer - returns bool) is performed on that.
# so you must be careful when chaining that the returned type has the method that you are calling next

print("\n!Chaining")
# When chaining your custom classes you need to make sure that it returns self
# You should be able to deduce know why this is.

class foo:
    def __init__(self, x):
        self.x = x
        
    def make_big(self):
        self.x *= 10
        return self
    
    def make_str(self):
        self.x = str(self.x)
        return self
    
    def is_str(self):
        return isinstance(self.x, str)

    def biggest(self, other):
        if self.x > other:
            return self.x
        else:
            return other

bar = foo(5)
bar.make_big().make_str()
# note that those functions are "in-place", they make changes without having to bar = bar.make_big()
print(bar.x, type(bar.x))
print(bar.is_str())
bar.make_big().is_str() # this works fine
try:
    bar.is_str().make_big() # doesn't work
except AttributeError:
    print("As is_str returns a Bool, it cannot be chained with make_big")

# There's an interesting interaction with make_str
# on the one hand
"""def make_str(self):
    return str(self.x)"""
# makes more sense, because it allows chaining of string methods e.g.
# bar.make_str().upper()
# on the other hand,
# bar.x = bar.make_str() is kinda dumb syntax (even in this shoddy example)

# Interestingly, strings are immutable so .upper actually returns a new string object back into the same place you stored the string
# This is handled automatically for convenience
# So the reason that .upper().split() works isn't because .upper() returns "self" but rather it's a string method that returns a string
# Which is functionally identical to return self (which returns the same object)
# so .make_big().make_big() works because the object going in has the method .make_big() as does the object coming out. 
# So If that makes it easier to think of chaining
# > Dot notation is evaluated left to right
# > dot notation requires the method/attribute to exist
# The second should be obvious - you can't call a function that doesn't exist.
# the first just means that bar.make_big().make_big() is the same as (bar.make_big()).make_big()


"Directed exercises"
# 1
# Make a function that calculates the factorial of a number
# n factorial (denoted n!) is equal to n * n-1 * n-2 ... * 2 * 1
# e.g. 5! = 5 * 4 * 3 * 2 * 1 = 120

# 2
# Using the following information, construct a guessing game
# info 1)
# input("string to print") # returns a <str> of whatever someone inputs in the console.
# also prints a string into the console on same line as input taken
# e.g. input("What is your favourite colour? ")
# out>>> What is your favourite colour? <input>

# info 2)
# The random module has a function called randint that generates a pseudorandom number between "start" and "stop" provided.


# 3
# How would you construct a virtual bar 
# Should include
# > Several different drinks served
# > A way to check customers age to not serve those underage
# > A way to charge customers for their drink
# > A rewards program (e.g. 10th drink free)

# (This is one I haven't actually built but I know how I would approach)
# If you need additional assistance then please contact George.Harpum while pleading the following
"Please George, I need a hint"



print("\n!Some other notes")

# Checking membership
# x in y 
# returns bool
# to check if an item is in an iterable
l = [x for x in range(5)] # making iterable
5 in l # False (recall range exclusivity)

# Timings
# For a list, each item has to be checked individually
# therefore, in the worst case, you have to check every item.
# The Big O notation then (a way for describing algorithm complexity) is O(n)

# Checking membership of a set is consant O(1)
# However, making sets is more intensive than a list

# for small list sizes 
l = [x for x in range(10)] # remember exclusive # takes ~734ns
9 in l # has to check everything ~201ns

s = {x for x in range(10)} # takes ~1050ns
9 in s # ~60ns

# O(n) where n is the input size, means that as the list and set get bigger, using the set gets better and better

l = [x for x in range(1_000_000)] # ~85ms
s = {x for x in range(1_000_000)} # ~90ms
assert 999_999 in l # ~15ms (mili) or 15_000_000 ns
assert 999_999 in s # ~ 83ns (nano)

# 15_000_000 / 83 = 180722.9 = 180_723x faster (but a list still only took 15ms)
# rather annoyingly caring about performance is a moot point
# generally, if your code can be improved massively you were doing something wrong in the first place.
# This isn't universal of course, there may be examples of improvement from one valid idea to another.


"Glob vs os"

# so Mike and I disagree on this but that's because he's wrong.
import glob
import os

# both of these are modules that help in reading files 
# glob allows for unix style file searching.

glob.glob("*.txt") # this reads the files in the default path (as none was given) that make the unix regular expression
# a regular expression (regex) is fancy string searching.
# python has another module called re that does similar for all strings.

# this * is a unix wildcard, so the function above matches any file that ends in .txt
# reasonable enough.

# os doesn't have a search function builtin
# however
[file for file in os.listdir() if file.endswith(".txt")]
# this is a list of all items in the (default) directory that end with .txt. 
# these are the same, except os is about twice as fast.

# for these instances I prefer os because, honestly, the os way is equally as readable to me.
# However, for more advanced regex I could see using glob

"Some words on if statements"

# If statements are great, vitally important in fact.
# However, there are some discussions over their implementation

# In python, there are so called "Truthy" and "Falsy" values.
# These are things which are treated as a bool, even though they are not.

# 0, empty data structures, empty strings,and None are all "Falsy" - they are treated as boolean false
# Everything else is Truthy - treated as boolean true

x = True
if x:
    pass
# This is completely valid because x is True. 
# However, some prefer the following
if x is True:
    pass
# the 'is' keyword is checking identity. 
# a is b MUST be the same object. 
# in this case, x is the object True so that works. 
# The above if statement is checking for boolean identify
x = 1 < 2
assert x is True # this works because 1<2 gets evaluated to True before assignment of x

x = ''
if x:
    pass
# this doesn't work because the empty string is considered false
x = 1
if x:
    pass
# this works because 1 is truthy
# however
x = 1
if x is True:
    pass
# This fails because x is not the object True, x is the object 1
l = []
if l:
    pass
# is convenient for testing whether your list is empty (after conditional appends, for example)
# But this isn't great practice. 
# mainly, because depending where l is defined, someone reading it doesn't actually know what it is
# is it a list, an integer, a boolean, etc.
if len(l) != 0:
    pass
# This at least says L is a data structure that has a size (still not perfect tbh)
# for custom implementations
class L(list):
    def is_empty(self):
        return len(self) == 0
custom_list = L((1,2,3)) # takes an iterable (this is only an example)
if custom_list.is_empty() is True:
    pass
# the if statement fails because the list is not empty
# It is clearer for custom objects, but len(list) == 0 is better for lists



"The futility of large if statements"

# Consider the following
# I want to assign a dispense pattern to plates in a project
# I have a list of all the individual wells in a project
# each row has the plate barcode and well ID (i.e. each row is unique)
# If I wanted to group some data together, e.g. by plate or assay, I can
# However, if I want to group by a dispense pattern, I would need to first assign it
# (Kraken export doesn't include the pattern it was dispensed in) 
# ((In a way it doesn't have to because the combination of plate and assay should be enough in most instances))
# (((it's fine for genotyping just not for manufacturing/R&D when testing different mixes)))
 
# I have made functions that can assign a dispense pattern based on well ID
# E.g., a hbq pattern can be assigned by row parity. 
# odd rows are HBQ_1 and even rows are HBQ_2 - very easy.
# But dispense ID is situational. I need to let the person decide which pattern to apply.

# I'll reveal the function in parts
def p1(pattern: str) -> None:
    if pattern == "Full":
        pass # imagine that I would assign the "full" pattern here
    elif pattern == "HBQ":
        pass
    elif pattern == "4tx":
        pass
    elif pattern == "4strip":
        pass
    elif pattern == "8strip":
        pass
    elif pattern == "16strip":
        pass
    else: 
        raise ValueError("pattern not recognised")

# This isn't too bad. 
# A bunch of if and elif statements, but there are only 6 options. 

# However - I cannot immediately assign the strips.
# While Full, HBQ, and 4tx are all plate agnostic, strips are not.
# Which wells are in a strip changes with whether the plate is 384 or 1536
# I have a function that identifies plate size. 
# It adds a boolean column with True for 1536 and false for 384
def p2(pattern: str) -> None: # just FYI it's returning none because the assigning is "in place"
    groupby = None # This is to prevent syntax errors, not part of the real function
    if pattern == "Full":
        pass
    elif pattern == "HBQ":
        pass
    elif pattern == "4tx":
        pass
    elif pattern == "4strip":
        for name, group in groupby.groupby("PlateSize"): # Pandas dataframes have a groupby method
            if name is True: # this is the value of the PlateSize (it does this for all groups)
                pass # 1536 assignment
            else:
                pass # 384 assignment
    elif pattern == "8strip":
        for name, group in groupby.groupby("PlateSize"): # Pandas dataframes have a groupby method
            if name is True: # this is the value of the PlateSize (it does this for all groups)
                pass # 1536 assignment
            else:
                pass # 384 assignment
    elif pattern == "16strip":
        for name, group in groupby.groupby("PlateSize"): # Pandas dataframes have a groupby method
            if name is True: # this is the value of the PlateSize (it does this for all groups)
                pass # 1536 assignment
            else:
                pass # 384 assignment
    else: 
        raise ValueError("pattern not recognised")
    
# You can see how this is starting to grow quite large
# I need to now explain how I'm assigning the pattern to show how this can be improved

map
# This is a builtin that computes a function with each element of an iterator
def add(n: int) -> int:
    return n + 1
print("mapping")
print(list(map(add,[0, 1, 2, 3]))) # map returns a map object (similar to how range returns a range object)
# Pandas (a module for data analysis) also has a map method
# A pandas Series is a 1 dimensional data structure (like a list) which some extras like a custom index and series name
# A pandas DataFrame is a 2 dimensional structure (It's a table)
# A column of a DataFrame is returned as a Series
# You have the row index as the series index, and the column title for the series title - it all works out
# You can map a function on a series with pd.Series.map (or .map after a series)
# Pandas also allows mapping of a dictionary (which python map doesn't)
# A dictionary is used as the basis of a replacement. 
# so a dictionary 
{0: 'a',
 1: 'b',
 2: 'c'}
# being mapped over a series
[0, 1, 2] 
# will return
['a', 'b', 'c'] 
# the important thing is that mapping a dictionary is fast.

# Making a dictionary in our case is also very fast because at most you have 1536 loops
# Computers can loop very fast.

# also note: .map RETURNS a value
# the returned value must be shoved anywhere.
# if you want to replace a column with values designated by a dictionary you do 
# Column = Column.map(dict)
# similar to how
add(1) # doesn't do anything - it needs to be put somewhere
x = add(1) # ta da!
# But, you can also put the returned value somewhere else
x = 1
x = x + 1 # x += 1
# or
x = 1
y = x + 1
# similarly
# A new column called "PatternID" is made with the results of the map
# The dictionary contains the wellID and the pattern it corresponds to
# e.g.
{"A01": "4tx1",
 "A02": "4tx2",
 "B01": "4tx3",
 "B02": "4tx4"}
def p3(self, pattern: str) -> None:
    """IN PLACE. Creates a new column ["PatternID"] and assigns a group based on well position."""
    data = None # solving the syntax error as pandas hasn't been imported
    self._plate_size() # assigns the plate size first. 
    if pattern == "Full":
        self.data["PatternID"] = "Full" # every well is a full plate well
    elif pattern == "HBQ":
        self.data["PatternID"] = self.data["DaughterWell"].map(self._hbq) # map the _hbq dictionary
        self._pattern_rename(self._P_HBQ)
    elif pattern == "4tx":
        self.data["PatternID"] = self.data["DaughterWell"].map(self._4tx) # map the 4tx dictionary
        self._pattern_rename(self._P_4TX)
    elif pattern == "4strip":
        self._plate_size()
        for names, _ in data.groupby("PlateSize"):
            if names is True:
                self.data["PatternID"] = self.data["DaughterWell"].map(lambda x: self._strips(x, 4, 32))
            else:
                self.data["PatternID"] = self.data["DaughterWell"].map(lambda x: self._strips(x, 4, 16))
    elif pattern == "8strip":
        for names, plates in data.groupby("PlateSize"):
            if names is True:
                self.data["PatternID"] = self.data["DaughterWell"].map(lambda x: self._strips(x, 8, 32))
            else:
                self.data["PatternID"] = self.data["DaughterWell"].map(lambda x: self._strips(x, 8, 16))
    elif pattern == "16strip":
        for names, plates in data.groupby("PlateSize"):
            if names is True:
                self.data["PatternID"] = self.data["DaughterWell"].map(lambda x: self._strips(x, 16, 32))
                self._pattern_rename(self._P_16STRIP)
            else:
                self.data["PatternID"] = self.data["DaughterWell"].map(lambda x: self._strips(x, 16, 16))
                self._pattern_rename(self._P_16STRIP)
    self.data["PatternID"] = self.data["PatternID"].astype('category')

# Lets ignore the lambda for now
# data is a class attribute that is a pandas DataFrame
# a column "PatternID" is being made (notice how it's being called like a data structure (i.e. with []))
d = {}
d["a"] = 1 # makes the key: value pair if it doesn't exist
# same with the column PatternID
# this PatternID is being made from the mapping of a dictionary over the DaughterWell (wellID) 
# The functions make the dictionary each time- because it's honestly easier than just having the dictionary pre-saved.
# the _strips takes the well ID (X) the number of strips it's meant to be (4, 8, 16) and then the number of rows
# (The above isn't the most recent version of the "bad" method - I did end up making some of those things easier.
# also, the reason _hbq and _4tx are left as function objects is because map calls the function object on each instance
# lambda x is used on strips because there are other parameters that needed to be defined.

# Long-story short - the above is uuugly.

def p4(self, pattern: str) -> None:
    pt = None # stop it complaining about the "Pattern dicT (pt)" module I made
    if not "PlateSize" in self.data.columns:
        self._plate_size() # if plate size doesn't exist, assign it
    size = 1536 # default plate size
    strip = None # will mention this later
    dict_ = {
        "hbq": pt.hbq,
        "4tx": pt.quads,
        "4strip": pt.strips,
        "8strip": pt.strips,
        "16strip": pt.strips
        }
    # This is a dictionary of function objects that could be called
    if pattern == "full": # if pattern is full, assign first 
        self.data["PatternID"] = "Full" # this is very fast so I wanted to keep it
        return self # prevents the rest of the code running (why check something you know will fail)
    if "strip" in pattern: # if the pattern has the word "strip" in it
        strip = pattern[:-5] # get the number by removing the last 5 characters (e.g., remove 'strip')
        # this allows me to get both single character (4, 8) and multicharacter (16) patterns out
        for name, group in self.data.groupby("PlateSize"): # loop over all 1536 plates (as one object) and then all 384 plates (max 2 loops)
            if name is False: # The function is the same for both 1536 and 384, just the parameter (size) has changed
                size = 384 # only needs to change the size for 384 plates
            self.data["PatternID"] = group.DaughterWell.map(dict_.get(pattern)(size, strip)) # DOUBLE BRACKETS ()()
            # Pandas has index matching so it updates data with the correct pattern for 1536 and 384 plates
        return self # stop function running after it has done strips
    # this will only run for 4tx and hbq as full and strip have returned by now
    self.data["PatternID"] = self.data.DaughterWell.map(dict_.get(pattern)(size, strip))
    return self

# so what is actually happening.
# dict_.get(pattern)(size, strip) # this is the bread and butter of the rewrite
dict # keyword
# trailing underscore is used to prevent keyword name clashing
# .get is a dict method for calling a value
# dict[x] == dict.get(x)
# .get is slightly better because it allows a default value
# dict.get(x, 0) returns 0 if x isn't a key in the dict (doesn't apply here)
# recall that the values of the dictionary are function objects
butts = str.upper
butts("hello") 
butts # function object of str.upper
# pt.hbq is the function object for the following 
# this gets imported from my module "pattern_dicts" as "pt" because "pd" is what pandas is imported as

def hbq(plate: int, *args) -> dict:
    """Creates dictionary of HBQ pattern assigned to each well 
    Parameters
    ----------
    plate : int
        Plate size by total number of wells.
    Raises
    ------
    PlateTypeError
        Errors if plate not 384 or 1536.

    Returns
    -------
    dict
        Each well with a HBQ pattern assigned""" # This is called a doc string
    if plate not in (384, 1536):
        raise PlateTypeError(f'Unsupported plate type: {plate}')
    row_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                   'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF']
    ncols = 48  # columns in 1536 plate
    dict_ = {}
    if plate == 384:
        row_labels = row_labels[:16]  # 384 has only 16 rows (A-P)
        ncols = 24
    for row in row_labels:
        for col in range(1, ncols+1):
            if ord(row[-1]) % 2 == 0: # 'a'[-1] is just itself. Check if the last character is odd or even
            # ord('A') = 65 (which is odd, as is 1).
                dict_[row + f"{col:>02}"] = "hbq2" # row = 'A': str + (str concatenate) '1' (that is formatted to pack a leading 0).
                # if col >= 10. there is no leading zero as it's packing 0's to len 2 (and it's already len 2)
                # str(col).zfill(2) does the same thing here, and they take the same amount of time.
            else:
                dict_[row + f"{col:>02}"] = "hbq1"
    return dict_

# just as 
hbq # is the function object without calling
# so to is dict_.get(pattern) 
# as I can put () after hbq for hbq()
# so too can I do
# dict_.get(pattern)(plate, strip)
# this is the same as
# hbq(plate, strip) 

# I've made hbq and quads (4tx) accept *args because strips NEEDS 2 inputs
# strips takes both plate size AND strip number
# if you try and insert a parameter where it's not wanted you'll produce an error
# but you can ask for a parameter that doesn't get used (although most of the time it's bad practice) 

# I could have made hbq take 'strips' and just leave it, but *args felt cleaner
# this way, not only have I cleaned up the if statements, it does also run a bit faster
# I'll leave working out what the HBQ is doing to you - contact me if you want to verify your thinking.

"How I added contents"
# I just think this is neat.
# Mike asked for a contents page (and I agreed)
# Adding it by hand was going to be a pain, but code can do it form me :D

# You might have noticed that most of the headings include "\n!" (the Bang (!) being a recent addition) 
# This is to allow for the heading to be slightly separated in the console
# But also allows for a unique identifier for the heading
try:
    with open(r'C:\Users\George.Harpum\Kraken script\explanation.txt') as file:
        for index, line in enumerate(file.readlines(), start=1):
            if r"\n!" in line: # ! added to find only headings and not normal \n instances
                start = line.find(r"\n!") + 3 # find gets the index of the start of the search string
                print(index, line[start:len(line)-3]) # line ends with ")\n
                # \n in the line is treated as a single special character
                # so len(line) - 3 is removing the newline, ) and " to leave just the title
                # This prints in the console a big ol' collection of line numbers and titles
                # I did then have to add the headings in and run it again, so the indexes included their own offset.
except FileNotFoundError:
    pass
# You should be able to work out why I've included a try block here, although I didn't use one when doing it for real
"with"
# I should explain this
# With is called a context manager

# open(file) returns a file object
# file = open(file)
# you can then do your file things as before
# However, you MUST remember to do file.close()
# if you don't - the file remains open by python (like how 2 people can't open the same file on a network drive)
# The context manager automatically handles the setup and teardown.
# this means you don't have to include .close()

# another example is os.scandir
import os
# with os.scandir('.') as files:
#     for file in files:
#         pass
# Although this is a poor example because it can also be treated easily without "with"

with os.scandir('.') as files:
    entries = [x for x in files] # files is lazy iteration and so can only be looped through once
    # saving it to entries allows entries to be used multiple times
    lengths = list(map(len, [x.name for x in entries])) # finds the longest name
    lengths.sort() # sorts small > large
    long = lengths[-1] # last item is the largest
    print("Name".center(long), "| is Folder?") # centres the name with the same length as longest item
    print('-'*(long+13)) # replicates '-' enough times to cover the longest item and "is folder?"
    for x in entries:
        print(x.name.ljust(long), "|", x.is_dir()) # ljust justifies (aligns) to the left with padding the same length as longest item

print("\nDone")

#%%
