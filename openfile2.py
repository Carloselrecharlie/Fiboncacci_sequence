
# with closes the file automatically after the indentention!!
# There are 2 ways to use it
with open("data/iris.csv.txt") as f: # f is the name we choose
  print(f.read())


# And this with an intermediate variable
with open("data/iris.csv.txt") as f:
  contents = f.read()
  print(contents)