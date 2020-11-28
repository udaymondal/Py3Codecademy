"""
#When we’re iterating through lists, we may want to skip some values. Let’s say we want to print out all of the numbers in a list, unless they’re negative. We can use continue to move to the next i in the list:

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
  if i < 0:
    continue
  print(i)

#Every time there was a negative number, the continue keyword moved the index to the next value in the list, without executing the code in the rest of the for loop.
"""

# Excercise

#Your computer is the doorman at a bar in a country where the drinking age is 21.

#Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print the age.

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i < 21:
    continue
  print(i)
