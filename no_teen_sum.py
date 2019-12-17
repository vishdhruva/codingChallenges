# Given 3 int values, a b c, return their sum.
# However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0,
# except 15 and 16 do not count as a teens.
# Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule.
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").

def fix_teen(n):
    if n == 13 or n == 14 or n == 17 or n == 18 or n == 19:
      n = 0
    return n
def no_teen_sum(a, b, c):
  a = fix_teen(a)
  b = fix_teen(b)
  c = fix_teen(c)
  return a + b + c
