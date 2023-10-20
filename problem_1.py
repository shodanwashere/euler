#!/bin/python

"""
If we list all the natural numbers below that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

mult = 0
multi = 1
multis = set()

# multiples of 3
while True:
  m3 = 3 * multi
  m5 = 5 * multi
  if m3 >= 1000 and m5 >= 1000:
    break
  else:
    if m3 < 1000:
      multis.add(m3)
    if m5 < 1000:
      multis.add(m5)
    multi += 1

print(sum(list(multis)))
