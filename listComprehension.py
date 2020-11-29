#We have defined a list heights of visitors to a theme park.
# In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters.
# Using a list comprehension, create a new list called can_ride_coaster that has every element
# from heights that is greater than 161.

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = []
"""
-----normally with for loop
for i in heights:
  if i > 161:
    can_ride_coaster.append(i)

print(can_ride_coaster)

-----using list Comprehension
"""

can_ride_coaster = [i for i in heights if i>161]
print(can_ride_coaster)