## using shell in Python 

- PS C:\Users\Prashant Deuja\OneDrive\Desktop\CSIT Notes\My_Learnings\Python> python
Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("chai")
chai
>>> 2+2
4
>>> ^Z

- PS C:\Users\Prashant Deuja\OneDrive\Desktop\CSIT Notes\My_Learnings\Python> python
Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> score =100 
>>> score
100
>>> tea
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tea' is not defined

- >>> import os
>>> os.getcwd()
'C:\\Users\\Prashant Deuja\\OneDrive\\Desktop\\CSIT Notes\\My_Learnings\\Python'
Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> for  c in "chai":
... print (c)
  File "<stdin>", line 2
    print (c)
    ^
IndentationError: expected an indented block
>>> for  c in "chai":
...     print(c)         
... 
c
h
a
i
>>> 

- import sys
>>> sys. platform
'win32'
>>> import first_program
MY first python code
Prashanta Deuja
>>>  first_program.name("i am a student")
  File "<stdin>", line 1
    first_program.name("i am a student")
IndentationError: unexpected indent
>>> import first_program
>>> from importlib import reload  
>>> reload(first_program)
MY first python code
Prashanta Deuja
<module 'first_program' from 'C:\\Users\\Prashant Deuja\\OneDrive\\Desktop\\CSIT Notes\\My_Learnings\\Python\\first_program.py'>
>>> first_program.name_one
'Niroj'


## Understandings Mutable and Immutable concepts in Python
-  python
- Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.>>> username = "Deuja"
>>> username
'Deuja'
>>> username = "chai"
>>> username
'chai'
>>> x = 20
>>> y = x
>>> x
20
>>> y
20
>>> x = 15 
>>> y
20
>>> 
