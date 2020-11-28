"""
1.
We have provided the list sales_data that shows the numbers of different flavors of ice cream sold at three different locations of the fictional shop, Gilbert and Ilbert’s Scoop Shop. We want to sum up the total number of scoops sold. Start by defining a variable scoops_sold and set it to zero.

Checkpoint 2 Passed
2.
Go through the sales_data list. Call each inner list location, and print out each location list.

Checkpoint 3 Passed
3.
Within the sales_data loop, go through each location list and add the element to your scoops_sold variable.

By the end, you should have the sum of every number in the sales_data nested list.
"""
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location_shops in sales_data:
  for listin in location_shops:
    scoops_sold += listin

print(scoops_sold)