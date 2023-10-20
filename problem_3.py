#!/bin/python3
import math
number = 600851475143

# first, generate primes.
sieve_final = list(range(2, math.floor(math.sqrt(number)) + 1))

# this cycle will generate the sieve of erasthotenes until the sqrt(n)+1
for n in sieve_final:
  i = 2
  while True:
    m = n * i
    if m < number:
      break
    sieve_final.remove(m)
    i += 1

factors = list()
for p in sieve_final:
  if number % p == 0:
    number = number / p
    factors.append(p)
print(sorted(factors)[-1])
