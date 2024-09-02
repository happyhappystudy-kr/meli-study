import sys
import re
input = sys.stdin.readline

equation = list(input().strip())
stacks = []
pairs = []
pat = re.compile("[0-9+*-/]")
for i, c in enumerate(equation):
    if pat.match(c):
        continue
    if c == "(":
        stacks.append((c,i))
    else:
        pairs.append([stacks.pop(), (c, i)])

from itertools import combinations
num_pairs = len(pairs)
ans = []
for r in range(1, num_pairs+1):
    for comb in combinations(range(num_pairs), r):
        equation_copy = equation.copy()
        for comb_idx in comb:
            p1, p2 = pairs[comb_idx]
            equation_copy[p1[1]] = ""
            equation_copy[p2[1]] = ""
        ans.append("".join(equation_copy))
ans = sorted(set(ans))
print('\n'.join(ans))