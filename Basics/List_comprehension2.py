carts = [['e','s','x'],['a','b','c'],['w','y','z']]

p1= ['e','s','x']
p2= ['a','b','c']
p3= ['w','y','z']

carts = [p1,p2,p3]

task_list = []
for row in range(0,25,5):
    inner = []
    for column in range(row,row+5):
        inner.append(column)
    task_list.append(inner)
for row in task_list:
    print(row) 


new_list = [[column for column in range(row,row+5)]for row in range(0,25,5)]  #[value to be added -- loop]

for row in new_list:
    print(row)
