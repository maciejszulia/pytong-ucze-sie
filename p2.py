import random

x = random.randrange(0, 10, 1)
y = random.randrange(1, 10, 2)

print(x)
if x % y:
    print("true")
else:
    print("false")

if x == y:
    print("x=y")
else:
    print("x!=y")

