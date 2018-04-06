# Carlos Montes Parra

# A program that displays a number from the Fibonacci sequence. The position 
# in the sequence is linked to the first and last letter of the user's name
# and the addition of their Unicode values.

# Adapted from one of Ian McLoughlin's lectures https://github.com/ianmcloughlin/python-fib/blob/master/fibname.py

def fib(n):
  # This function returns the nth Fibonacci number
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Montes"
first = name[0]
last = name[-1]
firstN = ord(first)
lastN = ord(last)
x = firstN + lastN

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstN)
print("The last letter", last, "is number", lastN)
print("Fibonacci number", x, "is", ans)

# SOLUTION

# My surname is Montes

# The first letter M is number 77

# The last letter s is number 115

# Fibonacci number 192 is 5972304273877744135569338397692020533504 

# ord () is a python built-in function which returns the Unicode value linked to a one-character string. It's the opposite of chr() or unichr()
