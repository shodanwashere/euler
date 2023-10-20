#!/bin/python

"""
If we list all the natural numbers below that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

sum = 0
mult = 0
multi = 1

# multiples of 3
while True:
  mult = 3 * multi
  if mult > 1000:
    break
  else:
    sum += mult
    multi += 1

multi = 1 # reset multiplier

# multiples of 5
while True:
  mult = 5 * multi
  if mult > 1000:
    break:
  else
    sum += mult
    multi += 1

print(sum)
