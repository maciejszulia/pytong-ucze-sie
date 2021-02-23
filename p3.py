import random

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

i = 0

for x in range(len(a)):
    if (a[x]) % 2:
        print(a[x])


def jezeli_prawda(a, b):
    if a == b:
        print("index of x equals x")
    else:
        print("index of x !equals x")


b = []
xx = 1
for xx in range(100):
    b.append(random.randrange(1, 100))
    print(xx, "=", b[xx], jezeli_prawda(xx, b[xx]))
