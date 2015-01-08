# A nested for loop to print out a checkered pattern of arbitrary size

size = 16 # This is the only variable that should be modified before running the code
one_line = ""
for i in range(0, size):
  for j in range(i, size + i + 1):
    if j == size + i :
      print one_line
      one_line = ""
    elif j % 2 == 0 :
      one_line += "#"
    else:
      one_line += " "
