# Introduction into Python

## Contents
1) [Basics](#Basics)
1) [Types](#Types)
1) [Operators](#Operators)
1) [Conditionals](#Conditionals)
1) [Variables](#Variables)
1) [Data Structures](#Data-Structures)
1) [Indexes](#Indexes)
1) [Loops](#Loops)
2) [Built-ins](#built-ins)
2) [Try block](#try-block)
3) 

Strings and Comments
Operators
String Operators
Variables
In place assignment operators
Types
Type hinting
Conditionals
If statements
Some keywords
Loops
Data Structures
Packing
Indexes
Slicing
Nesting
Iterables
Comprehensions
Functions and methods
Parameters
Returning
nth length parameters
Type checking
Wrappers
Class things
attribute vs method
Inheritance
Multilevel inheritance
Properties
Dataclasses
Built in methods
Importing
Chaining
Some other notes
```Python
print("Hello world")
```
# Basics
Python is a programming language that enables the execution of user-writen code.
Programming languages can differ greatly from each other. 
Python uses simple syntax (the way in which the language is written) which makes it a great language to learn for beginners.

This explanation assumes that you have already installed python and have a way to write code.

## How to write python
Python has "keywords". These are the words that have special meaning to python.
Examples include "if", "in", "assert"  "def", "class", and many more.
Python also has "built-ins" these are function python convenientally provides for us.
Examples include "print" which outputs to the console, "len" which gives the length of the a string or data structre, and many more.
Writing python involves creating "statements" from these keywords and built-ins that python can understand.
```Python
print
print("Hello")
```
In the above example the output is only "hello". This is because the first "print" built in function is not called. 
A function is called using parenthases '()'. The print function takes an input and attempts to display a str representation onto the console. 
Calling the function with no input outputs a blank line. 
```Python
print()
print("Hello")
# outputs:
#
# Hello
```
An important note, python will disregard anything after a '#'. This is called a comment and typically used to make the code more readable for others looking at the code.
An example
```Python
# prints the input back to the user
x = input("Please enter something")
print(x) # this prints x
```
Note that a comment can appear after a normal line of code. 

## Types
Programming languages need to know what types things are.
Python is a dynamically typed language. This means that whenever we use a type or object, python checks the type for us, so we don't have to.
For example, python knows that 10 is an integer.

### Some basic types
1. int
    * integer, a whole number such as 10, -7, 123456789
2. float
    * floating point number, a decimal number such as 1.0, 3.14159, 9.99
3. bool
    * boolean, a value that is True or False
4. str
    * String, declared with "" or '' can be comprised of any alphabet, numerical, or special character, "hello", '%', "1", " '' "

# Operators
## numerical operators
The numerical operators include
* \+
* \-
* \*
* \/
* %

/+ - * / all work as expected

'%' This is the modulo operator
This does exist in mathematics but it is less common.
The modulo can be thought of as the distance to the nearest divisor of a number. 
For example, 5 % 2 (said five mod two) is = 1 (This is because 5 is 4+1 and 4 is divisible by two)
```Python
assert 4 % 2 == 0
assert 10 % 3 == 1
```
Python also has a power operator: "\*\*"

Python is somewhat special in this sense, as not only is there a dedicated operator, it also functions completely as expected mathematically. 
For example
```Python
assert 2**2 == 4
assert 3**3 = 81
assert 9.0**0.5 == 3
```
Note well the final example, that any number (int or float) can be raised to the power of any number (int or float).
The use case for this will most often be the convenient square rooting of a number (x to the power of 1/2).


## string operators
Both '+' and '*' have string implementations
These concatenate and multiple strings respectively.
```Python
assert "Hello" + "World" == "HelloWorld"
assert "hi" * 3 == "hihihi"
```
Notice that '+' only works between two strings, and that '*' only works between a string and an integer.

# Conditionals
These are statements which evaluate down to a boolean (True or False).
## Conditional operators
* Less than <
* less than or equal <=
* greater than >
* greater than or equal >=
* equal to ==
* not equal to !=

Throughout this document I use the "assert" keyword in the python code snippets. 
```Python
assert True
```
if assert is True then the code does nothing.
If assert is False then it raises an AssertionError, a special type of error that says that whatever was after assert was false.
The practical use of this is testing stages of a larger function (and finding when it doesn't meet your expectations).

Python kindly evaluates expressions for us. With this, we can use a conditional with assert
```Python
1 + 1 == 2 # Evaluates to True
assert 1+1 == 2 # Evaluates to True, and as previous, assert True continues 
```
# Variables
Variables serve two primary purposes. 
1. They act as placeholders for values
2. They save having to repeatedly compute the same information

A variable can be assinged with the '=' operator.
```Python
x = 1
y = 2
x = 3 # overwriting value
print(x)
print(y)
```
The ability to refer to 'x' throughout the code is invaluable, as it allows for the easy modification of the value of x.
Consider the following
```Python
print(1)
print(1+1) 
print(1**2)
print(14 - 1)
```
But alas! after all that work you didn't mean to put 1, you really meant 2! 
Now in this example it's 4 lines and 5 instances of '1'. But what if you miss an instance?
This is a rather simple example that does not fully do justice to the raw importance of having instances of values.

The use of variables allows for generalised code to treat any value in the same way
```Python
x = int(input("What number would you like to use?"))
print(x**2 + 2*x + 1)
```

## In place assignment

Now that we have a variable we might want to do something with it
For example
```Python
x = 1
y = x + 1
```
Say we have a value that we want to increment. We want to increase our original value by one. 
In the above method we've had to use a secondary variable, but there's no reason why this must be the case. 

As long as a variable exists when it is being called, it can be used. 
For example
```Python
x = 1
x = x + 1
```
Python evalutes expressions down to a single value first. Therefore, x+1 first calls the value of x before python looks at the left hand side.
This is the same evaluation happening below
```Python
x = 1
y = x + 1
```
So first the expression is evaluated, then once it has a value it can assign (in the above case 2), it looks at the location of the assignment.
we're assigning the value 2 to 'x', which overwrites whatever was there. 
Had the first line not existed the code would produce an error. 
Specifically a NameError, as name 'x' is not defined. 

When assigning to the same variable, python has a helpful shorthand. 
These are the in-place assignment operators.

```Python
a = 1
a += 2
assert a == 3
a *= 3 
assert a == 9
a -= 4
assert a == 5
a /= 5
assert a == 1
```
There are also the %= and **=, however I find fewer use cases for these. 

# Data Structures
Data structures (or containers) are special structures which contain multiple values in one variable.
## Types
Python contains four primary data structures.
1. List
2. Tuple
3. Dictionary
4. Set
Each of these have their own advantages and disadvantages and are used in different situations.

## Lists
Lists are defined with [] or the function list.
```Python 
l = [0, 1, 2, 3]
l = list((0, 1, 2, 3))
```
Lists are 
1. Mutable
2. Ordered
Mutable means that their contents can be changed after initialisation
using 'dot notation' on the list object allows for 'appending' (a list specific term)
```Python
my_list = [1]
my_list.append('a')
assert my_list == [1, 'a']
```
Append, as the name suggests, appends the item onto the end of the list.

Lists are also ordered, meaning that the order of the items is preserved.
```Python
list_1 = [1, 2, 3]
list_2 = [2, 3, 1]
assert list_1 != list_2
```
The lists are not considered equal because the order of the lists does not match

The order is preserved with an [Index](#indexes)
Lists are generally used for homogenous data, although that is convention. 

# Tuples
A tuple is declared with '()' and is 
1. Ordered 
2. Immutable

Similar to lists, elements of a tuple can be any object (int, str, functions, classes, lists) and where the order matters.
However, tuples are immutable. They cannot be altered after initialisation.
```Python
t = (1, 2, 3)
t2 = (3, 2, 1)
assert t != t2 
try: 
    t[0] = 'a'
except TypeError:
    print("A tuple cannot be modified")
print(t)
```

# Indexes
When dealing with data structures indexes start at 0.
If this is enough for you to understand how they work or at the very least to live with this fact you can continue on to the next section.
If not, then this might be helpful. 
In short, indexes start at 0 because it allows programmers to have one extra item their lists. 
The longer reason for this is that computers function with binary. Binary is a method of counting in a base 2 system.
Each unit of a binary number can be thought of signalling whether a power of 2 is present.
This starts with two to the power of 0. Any number to the power of 0 is 1 so the binary number 001 tells you that there is no 2^2^, there is No 2^1^ but that is 2^0^, which is 1. 
Because of this a binary number of N digits can represent all numbers from 0 (all 0's) up to 2^n-1^.
This is because, to represent 2^n^ would require the "ticking over" into an additional unit that would be for example.
1111 in binary is equal to 15 (2^0^ + 2^1^ + 2^2^ + 2^3^).
To represent 16 (2^5^) a new digit needs to be added.
Having access to a range of numbers 0 -> 2^n-1^ actually allows you access to 2^n^ items if you count 0 as one of them. (This could also be thought of as n+1 for all n in the range).

# Loops
Loops are blocks of code that repeatedly execute until some condition is met.
## While loops
while loops are if statements which repeatedly check a boolean condition until it is false.
Consider the if statement below
```Python
x = int(input("Enter a number")
y = int(input("Enter another number")
if y == 0:
    y = int(input("Please enter a number that isn't zero"))
print(x / y)
```
Dividing any number by 0 is undefined (this is a maths thing). Attempting to divide by 0 in python will produce an error.
The above if statement is trying to prevent the division by 0 error, but a user may input 0 a second time.
One method to prevent this is by using a while loop
```Python
x = int(input("Enter a number")
y = int(input("Enter another number")
while y == 0:
    y = int(input("Enter a non-zero number")
print(x / y)
```
If y is 0, the while loop will continually ask for an input until y == 0 is false.

Another common use of a while loop is to have a counter.
```Python
i = 0
while i < 5:
    print("again")
    i += 1
```
It is very important to always include the counter incrementation.
Without it, i will **always** = 0, and so the condition i < 5 will **always** be True. 
This creates an infinite loop which will never end without cancelling (Control-C will stop the code running if this happens to you).

## For loops

For loops iterate over each item in a container. They stop when they've looped over the last item, or, in other words, they loop len(List) times. 
```Python
l = list(range(5))
for x in l:
    print(x)
```
As this code runs, the for loop takes the first value of the list and assigns this to x. Then, in this example, it prints the value of x.
At the end of the block, if there are more items in 'l', x gets assigned the next time and the block of code is repeated. 

This can be thought of in several ways.
Firstly, imagine a bucket. That bucket is the container 'l'. Inside the bucket are all the contents of 'l'.
the for loop is taking an item out of the bucket, performing some action with the item, and then it throws it away (putting it outside of the bucket).
The for loop continues until the bucket is empty.

Another approach would be to consider a for-loop as an incremental index. Implementing this idea using a while loop produces the code below.
```Python
l = list(range(5)) # [0, 1, 2, 3, 4]
i = 0
while i < len(l):
    x = l[i]
    print(x)
    i += 1
```
However, this requires 4 additional lines over the existing for loop, and so it's clear why using "for" can be easier. 
Using "for" over "while" is so much easier, in fact, that some people use it even when they don't need the item from the list!
Let's say you want to print the same message 3 times. 
```Python
i = 0
while i < 3: # 0, 1, 2 cause prints (= 3 times total)
    print("Hello again")
    i += 1
```
This can also be done with
```Python
for x in range(3)
    print("Hello again")
```
Notice how that uses fewer lines and required less typing. 
Another important thing to notice is that the 'x' variable is still being assigned.
If, after running that code, you included 'print(x)' (outside the loop) you'll see the program print "2" in the console.
In cases where the variable is not being used in the loop, it's convention to include an underscore '_'
```Python
for _ in range(1):
    print("Like this!")
```
