# Challenge Briefing
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

# Use of a Lambda here - lambda arguments : expression
def main(number, func = None):
   if func:
      return func(number)
   else:
      return number

# Numbers
def zero(func=None): 
   return main(0, func)

def one(func=None): 
   return main(1, func)

def two(func=None): 
   return main(2, func)

def three(func=None): 
   return main(3, func)

def four(func=None): 
   return main(4, func)

def five(func=None): 
   return main(5, func)

def six(func=None): 
   return main(6, func)

def seven(func=None): 
   return main(7, func)

def eight(func=None): 
   return main(8, func)

def nine(func=None): 
   return main(9, func)

# Calculations
def times(x): return lambda y: y * x
def divided_by(x): return lambda y: y//x
def plus(x): return lambda y: y + x
def minus(x): return lambda y: y - x

