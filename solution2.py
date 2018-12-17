from collections import Counter

N = int(raw_input())

C = map(int, raw_input().split(' '))

c = Counter(C)
s = 0
for i in c:
    s += c[i]/2
print s
