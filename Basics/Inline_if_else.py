a = 20
if a == 20:
    print('a 20')
else:
    print('no')

print('a is 20' if a == 21 else 'a is not 20')

b = True if a == 20 else False
print(b)

num = [value for value in range(-5,5)]
print(num)

pos = [value for value in num if value > 0]
print(pos)