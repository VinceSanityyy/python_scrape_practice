import random

list = []
for value in range(0,20):
    list.append(random.randint(0,100))
print(list)

new_list = [value for value in range(0,20)]
print(new_list)

new_list = [random.randint(0,100) for value in range(0,20)]
print(new_list)