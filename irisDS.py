
# Carlos Montés Parra

import csv


with open('data/iris.csv', newline='') as csvFile:


  for line in csvFile:
    
    line = line.replace(',', ' ') #removes the comma separating the numbers

    a = float (line.split()[0]) #converts strings into values so I can make operations later on
    b = float (line.split()[1]) # print(type(a)) confirms it
    c = float (line.split()[2])
    d = float (line.split()[3])

    print(line[:3]+ '      ' + line[4:7]+ '      ' + line[8:11]+ '      ' + line[12:15]) 


  
    
  