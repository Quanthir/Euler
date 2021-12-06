#!/usr/bin/env python
def F():
    a, b = 0, 1

    while a < 4000000:
        yield a
        a, b = b, a + b

count = 0
for f in F():
    if f % 2 == 0:
        count += f

print(count)

# One Liner
print(sum([f for f in F() if f % 2 == 0]))