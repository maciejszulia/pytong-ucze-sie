import random

my_list = [1, 2, 3, 4, 5, 6, 7, 8, "Maciek", [0, 1, 2, 3, 4, 5]]

x = 0
for x in range(100):
    my_list.append(random.randrange(100))

for element in my_list:
    print(element)
