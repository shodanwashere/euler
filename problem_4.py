#!/bin/python3

p1 = list(range(999, 100, -1))
p2 = list(range(999, 100, -1))
palindromes = set()

exit = False
for m1 in p1:
    for m2 in p2:
        p = m1 * m2
        # get digits
        p_digis = list()
        i = 10
        while p > 0:
            p_digis.append(p % i)
            p //= i
        result = all(x == y for x, y in zip(p_digis, reversed(p_digis)))
        if result:
            palindromes.add(int("".join([str(x) for x in p_digis])))
print(max(palindromes))
