import csv



with open('data/iris.csv', newline=' ') as csvFile:

  for line in csvFile:

    line = line.replace(',', ' ') #no comma separating the numbers

    print(line[:3]+ '      ' + line[4:7]+ '      ' + line[8:11]+ '      ' + line[12:15]) 