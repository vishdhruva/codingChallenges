# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each) and big bricks (5 inches each).
# Return True if it is possible to make the goal by choosing from the given bricks.

def make_bricks(small, big, goal):
  total = 0
  needed = 0
  i = 0
  while (total <= goal and i <= big):
    needed = goal - total # sees how many bricks are needed
    if (small >= needed): # checks if small bricks can cover remaining amount
      return True
    else:
      total += 5 # if small cannot cover amount then add a large brick(5)
    i+=1 # counter to ensure bricks given >= bricks used
  return False
