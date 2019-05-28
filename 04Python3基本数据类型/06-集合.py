#!/usr/bin/python3

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)

if 'Jim' in student :
    print('Jim 在集合student中')
else :
    print('Jim 不在集合student中')

# set可以进行集合运算
setA = set('werafasdf')
setB = set('wegfdbfggxzcv')

print(setA)
print(setB)

print(setA - setB)  # A 和 B 的差集
print(setA | setB)  # A 和 B 的并集
print(setA & setB)  # A 和 B 的交集
print(setA ^ setB)  # A 和 B 中不同时存在的元素
