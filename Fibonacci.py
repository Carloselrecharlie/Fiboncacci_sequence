# Carlos Montes Parra

# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
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
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# SOLUTION

# My surname is Montes

# The first letter M is number 77

# The last letter s is number 115

# Fibonacci number 192 is 5972304273877744135569338397692020533504 

# ord () is a python built-in function which returns the Unicode value linked to a one-character string. It's the opposite of chr() or unichr()
