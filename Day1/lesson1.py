
''' Part 1: Hello World'''
# Hello World!
# This is my first Python Program
# How do I make the computer say "Hello World"?
print ('Hello World')
# Can you change this to say your name?
print ('My name is Brandt')

''' Part 2: Spacing? '''
print('\nSpaces?\n')

# Here's something to notice, the amount of space between
# Print and the first '(' doesn't really matter
print ('1. Hello World')
print         ('2. Hello World')
# Even between the parentheses
print (    '3. Hello World'     )
print ('4. Hello World'    )
print (   '5. Hello World')
# Or between lines
print ('6. Hello World')


# Python doesn't care that we've left all this space between lines
# That's because it just ignore empty lines


print ('7. Hello World')
# You can also use double quotes if you like
print ("Hello world")

# However it's important to know that spaces before lines
# are something you should be careful about.
# Python uses a special indentation system and spacing before lines needs
# to be done in a specific way. We'll talk about this later.
# For example: remove the '#' from the next line and run the code, you'll get an error

#  print ("Hello World")

''' Part 3: Printing numbers and Text '''
# As we already know print can use text
print("What is the answer to life?")
# The print can also use numbers
print(42)
print(3.56)


''' Part 4: Comments '''

# If you haven't noticed by now, you can put a '#' before a line to tell
# Python to ignore that line. Lines that start with a '#' are called comment lines or
# comments.
# This following line is a line of code, however, it starts with a '#' so it won't run

# print ('Hello World')

# Most coding editors will color comment lines different than code lines so it's
# easy to tell.

''' Did you notice that comments can also be down by using three single quotes? '''

'''
  Comments using three quotes can comment out multiple lines at once.
  Thus why I can write this little blurb without having to keep adding a '#'
  at the beginning of each line.
'''

"""
  You can also use three double-quotes to achieve the same function as the " ''' "
"""

# Remember that the """ and ''' will comment out everything until the next """ or '''
# is seen.

