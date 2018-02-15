# Carlos Montes
# Even numbers are divided by 2 and odds multiplied by 3 then +1

n = input("Choose a natural integer greater than 1 to execute the Collatz conjecture please ") #Prompt

myInput = int(n) #To turn the user input string into an integer

print (myInput)

count = 0 # The counter of the number of times the while loop runs starts

while myInput > 1 : 
    count += 1 # Increments by 1 every time it loops
    if (myInput % 2 == 0) : 
        e = myInput / 2
        print ( int (e) ) # with int we take only the integer part
        myInput = e
    else:
        o = myInput * 3 + 1
        print ( int (o) )
        myInput = o

print("It took" ,count, "iterations to reach number 1") # commas are requiered to separate text 
# from strings while printing. They also add a single space.
