board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

# This is the basic loop format
""" -----
for <temporary variable> in <list variable>:
    <action>
---------- """
for game in board_games:
    print(game)

for sport in sport_games:
    print(sport)

"""
------ Use the range function in a for loop to print out promise 5 times
"""
promise = "I will not chew gum in class"

for i in range(5):
  print(promise)

