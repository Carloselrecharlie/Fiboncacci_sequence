# Carlos Montes Parra 21/02/2018

# the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20? https://projecteuler.net/problem=5 

n = 1
r = 1

while r != 0: # loop that runs until the reminder from the for loop is not equal to 0 (not divisible)

  for i in range(20): # every natural number is divided by the range 1 - 20 one at a time

    r = n % (i + 1)
    
    if r != 0: # to stop the for loop and move on to save unnecessary iterations
      break

  n = n + 1 # increment

print("The smallest positive number that is evenly divisible by the first 20 natural numbers is", n - 1)
