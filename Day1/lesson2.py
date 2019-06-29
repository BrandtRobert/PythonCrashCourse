''' Part 1: Numbers and Assignment '''

# Here we are storing some numbers in python
# Now in programming languages it's important to know that
# the '=' doesn't ask the question "is equal to?"
# It rather says "set this variable equal to", or "store this value in here"

x = 1  # This statement tells python store the number '1' in the variable called 'x'
y = 2  # This statement tells python to store the number '2' in the variable called 'y'

# Let's print these out just to verify
# Notice that if we just put in 'x' or 'y' we don't use quotes

# Also I am adding a few print statements to make it easier to read on the console
# output. You don't have to understand these right now

print('Value of x: ', end='')  # Ignore this statement for now
print(x)  # Prints out 1
print('Value of y: ', end='')  # Ignore this statement for now
print(y)  # Prints out 2

# Here's another cool trick that can be done
x = y
# So what is the value of 'x' going to be now?
# Let's check by printing out what's stored in x
print('Value of x after "x=y": ', end='')  # Ignore this statement for now
print(x)
# How did 'x' become '2'? We'll the statement 'x = y' tells python to
# take whatever is in y and put it in x

''' Part 2: Python data types '''

'''
  Now obviously if wanna build a game we need more than just the ability to print
  out numbers and text. We need to be able to do calculations, and store data.
  In python we have something called data types. Data types are exactly as they sound the
  different types of data the exist in a coding language.
  What could you come up with if thought of different types of data? Maybe you are makng 
  a survey and the participants are going to have to answer some questions?
  You might have several types of survey questions:
    * True / False
    * Short answer or text answers, like free response
    * Numerical questions like "How old are you?", "How many miles do you drive a day?"

  You can think of data types in a very similiar fashion
'''

""" Integer """
# We've already seen the numerical data type
# This data type is reffered to as an integer (a postive or negative whole number)
print('\nValue of x: ', end='')  # Ignore this statement for now
x = 54
print(x)
print('Value of z: ', end='')  # Ignore this statement for now
z = -54
print(z)

# Let's look at some other fundamental python data types

""" Floating Point"""
# Here is the floating point data type. It's kind of a weird name but it means
# that it's a data type that has a decimal point in it. The name comes from a certain
# computer engineering specification that's kind of complicated
pi = 3.14
print('\nValue of pi ', end='')  # Ignore this statement for now
print(pi)
d = -780.97
print('Value of d ', end='')  # Ignore this statement for now
print(d)

""" Boolean """
# Here is the boolean data type. It's a fancy name for True/False
# It's named after English mathematician George Boole
# who's ideas were a fundamental force in computer science and logic
a = True
b = False
print('\nValue of a: ', end='')  # Ignore this statement for now
print(a)
print('Value of b: ', end='')  # Ignore this statement for now
print(b)

""" String """
# Here is the string data type. You can think of it as text. It's short for
# 'string of characters'. And in python you might see it referred to an even shorted name
# 'str'
h = 'Hello'
g = 'Banana'
print('\nValue of h: ', end='')  # Ignore this statement for now
print(h)
print('Value of g: ', end='')  # Ignore this statement for now
print(g)