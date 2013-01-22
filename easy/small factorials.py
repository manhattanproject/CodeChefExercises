from math import factorial

t = int(raw_input())
c = 0
s = []

while c < t:
  n = int(raw_input())
  r = factorial(n)
  s.append(r)
  c += 1

for i in range (0, len(s)):
  print s[i]

exit(0)
