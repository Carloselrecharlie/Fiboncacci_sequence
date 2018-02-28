f = open("data/iris.csv.txt")
# we name it as f

print(f) #outputs some info from the file

print(f.read()) #this prints the content

f.close() # every file should be closed before exiting CSV
