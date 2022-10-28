'''
Text Type (String)
'''

# s = "This is a single line string"
# print(s)
# print(type(s))

# =========================

# s = """this is a multiline string example"""
# print(s)
# print(type(s))

# =========================

# find a character by index
# s ='string'
# print(s[5])

# slicing
# s = 'string sample'
# print(s[1:6])

# =========================
# immutable (EXPLAIN PLEASE??)
# s = 'string sample'
# s[2] = 'o'
# print(s)

'''
Numeric Text Type (Integer, Float, Complex nos)
'''
# x = 1234534567459586
# print(type(x))

# accurate up to 15-16 decimal places
# x = 0.1234567898765432123445334
# print(type(x))
# print(x)

# x = 1+2j
# print(type(x))

'''
Sequence Type (List, Tuple, Range)
'''
# homogeneous - List tend to have mostly the same data type in them  
# List
# x = [10, 2.5, 'hello']
# print(x[2]) 
# print(x[1:3])

# mutable (a sring is mutable)
# x[2] = 'Python'
# print(x)

# Tuple 
# heterogeneous - i.e can have different types in there
# tuple = ()
# tuple = ("cat",[4,3,2], (1,2,3))

# =========================
# both of examples below are type tuples, without comma makes it a string. 
# tuple = ("hello",)
# tuple = "hello", 
# print(type(tuple))

# =========================

# tuple = ("cat",[4,3,2], (1,2,3))
# print(tuple[2])

# =========================

# Immutable - tuples are immutable

# tuple = ("cat",[4,3,2], (1,2,3))
# tuple[2] = 10
# print(tuple)

# =========================

# Range - Always length of defined figure minus 1, and starts from 0

# x = range(10)
# for n in x:
#  print(n)

'''
Mapping Type (Dictionary)
'''
# Comes in handy for things that have a key and value
# dict = {}
# print(type(dict))

# =========================
# dict is mutable (Has key and value)
# dict = {'name': 'Kingsley', 'age':37}
# print(dict['age'])

# print(dict.get('name'))

# dict['age'] = 26
# print(dict)

'''
Set Types
'''

# set looks a bit like dict with the {} symbol BUT set has Values ONLY
# BUT if use {} when its empty its a dictionary NOT a set

# ALSO set does not support indexing

# set = {}
# print(type(set))

# can also do like below 
# empty set having set = {} is an empty dict
# set = set()
# print(type(set))

# =========================

# mixed data types (all immutable)
# set = {3.2, "hi", (1,2,3)}
# print(type(set))
# # TypeError: 'set' object is not subscriptable (means cant be indexed)
# print(set[0])


# =========================

#  set cannot contain the same element twice. That is no duplicates allowed. So wont print dups as below

# set = {3.2, "hi", (1,2,3), "hi"}
# print(set)

# # =========================
# # cannot have mutable (e.g. a list) in a set
# set = {3.2, "hi", (1,2,3), [1,2,3]}
# # unhashable type: 'list'
# print(set)

'''
Boolean Type (True or False)
'''

# print(type(True))

#  boolean as numbers
# print(True == 1)
# print(False == 0)

# intresting logic
# print(True + True)

# not boolean operator
# print(not True)
# print(not False)

# and boolean operator (presence of false will always give false)
# print(True and False)
# print(True and True)
# print(False and False)
# print(False and True)

# or boolean operator (presence of True will always give True???)
print(True or False)
print(True or True)
print(False or False)