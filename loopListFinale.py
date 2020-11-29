single_digits = list(range(10))
print(single_digits)
squares = []
for i in single_digits:    # squaring list in for loop
  print(i)
  i = i**2
  squares.append(i)
print(squares)

cubes = [i**3 for i in single_digits]   #cube_list using comprehension
print(cubes)