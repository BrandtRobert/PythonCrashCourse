'''Part 1: Mathetmatical Operations '''

''' 
  In the last section we talked about data types. Here we are going to review
  some mathematical operations. Mathematical operations allow us to operate on variables
  using ideas we already know from math like: '+', '-', '*', etc
'''

# Let's define some variables first
x = 5
y = 7
c = 1.5
d = 2.0
string1 = 'Hello'
string2 = 'World'

''' Add and Subtract '''
# We can add things very easily by using '+', now we are going to be wrapping things in
# print so you can see

print (x + y)
print (c + d)

# We can also add data floating point to integer if we want
print (x + c)

# We can also add strings together if we want
print (string1 + string2)
# Notice how they get smashed together,
# if we want a space in between we have to explicitly add one
print (string1 + ' ' + string2)

# We can also subtract
print (y - x)
print (d - c)

# But substract doesn't work on strings. Try uncommenting this line and find out
# string1 - string2

''' Multiply and Divide '''
# Multiply and divide works just like a calculator as well
# Let's define some variables first
x = 15
y = 3
c = 12.0
d = 0.5

print (y * x)
print (x / y)
print (c * d)
print (c / d)
print (d * x)

# We can also do funny stuff with strings and multiply.
# Since remember that multiply is really just adding something to itself.
# Here we add hello to itself 3 times
string1 = 'hello '
m = 3
print (string1 * m)

''' Power Operator '''
# Using ** as an operator signals to raise something to the power of something else
x = 2
y = 5
d = 0.5

print (5 ** 2)
print (x ** 2)
print (x ** y)

# Remember that fractional powers are like taking a root of something
print (25 ** d)