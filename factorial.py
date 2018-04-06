# Carlos Montes 12/03/2018
# This program returns the factorial of a positive integer

def factorial(x):
  y = 1
  for i in range(x, 1, -1): # iterates multiplying the argument by
    # all the smaller natural integers to it, down to 2 
    y = y * i
  return y

# In these examples we call the function from within the print statement
print(f"The factorial of 5 is {factorial(5)}")
print(f"The factorial of 7 is {factorial(7)}")
print(f"The factorial of 10 is {factorial(10)}")




