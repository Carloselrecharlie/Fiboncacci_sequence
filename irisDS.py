
# Carlos Montés Parra

# The point of this piece of code is to display only the figures from a data file on the screen

import csv # since we are handling a csv file


with open('data/iris.csv', newline='') as csvFile: # Opening the data file


  for line in csvFile: # This for loop iterates through the whole file line by line
    
    line = line.replace(',', ' ') # removes the comma separating the numbers

    a = float (line.split()[0]) # converts strings into values so I can make operations later on
    b = float (line.split()[1]) # print(type(a)) confirms it
    c = float (line.split()[2])
    d = float (line.split()[3])

    print(line[:3]+ '    ' + line[4:7]+ '    ' + line[8:11]+ '    ' + line[12:15]) 
    # Introduced 4 white spaces between column and column

  
    
  