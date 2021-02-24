import random

list1 = []
list2 = []

# for i in range(0,1,1):

# convert list to ints by using map
test_list1 = list(map(int, list1))
test_list2 = list(map(int, list2))

for i in range(0, len(list1)):
    list1[i] = int(list1[i])

for x in range(0, random.randrange(1, 20)):
    list1.append(random.randrange(0, 10))

for i in range(0, len(list2)):
    list2[i] = int(list2[i])

for x in range(0, random.randrange(1, 20)):
    list2.append(random.randrange(0, 10))

print("list1: " + str(list1))
print("list2: " + str(list2))

#temp_list1

dl = abs(len(list1) - len(list2))
print(len(list1), " ", len(list2))
print(dl)

i=1
for i in range(dl):
    if len(list1) < len(list2):
        list2.pop(i)


print(len(list1), " ", len(list2))


for i in range(0, len(list1)):
    if list1[i] == list2[i]:
        print(list1[i], "true", list2[i])
    #else:
     #   print(list1[i], "false", list2[i])