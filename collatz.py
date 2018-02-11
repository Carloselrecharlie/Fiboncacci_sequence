# Carlos Montes
# In the Collatz conjecture even numbers are divided by 2 and odds multiplied by 3, then +1

n = 17

print (n)

count = 0 # The counter of the number of times the while loop runs starts

while n > 1 : 
    count += 1 # Increments by 1 every time it loops
    if (n % 2 == 0) : 
        e = n / 2
        print ( int (e) ) # with int we take only the integer part
        n = e
    else:
        o = n * 3 + 1
        print ( int (o) )
        n = o

print("It took" ,count, "iterations to reach number 1") # commas are requiered to separate text 
# from strings while printing. They also add a single space.
