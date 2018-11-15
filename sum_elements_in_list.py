simple_list = [1, 2, 3, 4, 5]

# 1.) use for loop

amount = 0
for number in simple_list:
    amount = amount + number
print(amount)   

# 2.) use while loop

total = 0
i = 0
while i <= len(simple_list):
    total = total + i
    i = i + 1
print(total)    

# 4.) 1*2, 2*2, 3*3, 4*4, 5*5 use lambda function

new_list = list(map(lambda number: number*2, simple_list))
print(new_list)

# 5.) sum numbers in list / use reduce

import functools 

new_list = functools.reduce(lambda acc,v: acc + v, simple_list, 0)
print(new_list)


