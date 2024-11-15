#скачанные библ
# import 

#встроенные библ
from math import *
import math

#разработнные библ
from dicts import helloWorld

# print(dir(math))
# help(math.sin)

import random
print(random.random())

def fact(x):
    res = 1
    while x>0:
        res*=x
        x-=1
    return res

def fact2(x):
    res = 1
    for i in range(1, x+1):
        res*=i
    return res

# print(fact2(5))
# print(fact(3))

def some_func(a):
    if type(a) == list:
        a.append(1)
        return a
    else:
        return []

# print(some_func([]))

b = 1

def custom_max(*a):
    my_max = a[0]
    for i in a[1:]:
        if i>my_max:
            my_max=i
    return my_max

# print(custom_max(1,2, 2,4,6,7,8,1))



add_three_calls = 0
def add_three(number):
    global add_three_calls
    # print(f'Returning {number + 3}')
    add_three_calls += 1
    return number + 3

a = 3
v = add_three(a)


# -----------------------------------------------------
# wallet

def add_balance(x):
    global balance
    balance+=x

def sub_balance(x):
    global balance
    if balance-x<0:
        print('Баланс не может быть отрицательным')
    else:
        balance-=x
    

def wallet():
    while True:
        command = input('Введите команду: ')
        if command == 'add':
            inp = int(input())
            add_balance(inp)
        elif command == 'sub':
            inp = int(input())
            sub_balance(inp)
        elif command == 'exit':
            break
        else:
            print('Введите корректную команду')
        print('Ваш баланс: ', balance)
        print('------------------------------')
            

balance = 0
# wallet()

# ----------------------------------------------------------

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp-1)
#----------------------------------------------------

def summ(a,b):
    if a == b+1:
        return 0
    return a + summ(a+1, b)

# print(summ(3,5))

#-------------------------------------------------------

double = lambda x: x*2  

def double(x):
    return x*2
    
lst=[4,56,98,52,963,741,25,8, 2.2, 23.5]
newlist=list(filter(lambda n:type(n)==int,lst)) 
print(newlist)

lst=[4,56,98,52,963,741,25,8]
newlist=list(map(double,lst)) 
# print(newlist)

lst=[4,56,98,52,963,741,25,8]
newlist=list(map(lambda n:n%2==0,lst)) 
# print(newlist)

import functools 
lst=[4,56,100]
ld=functools.reduce((lambda x,y:x+y),lst) 
# print(ld)

tbl=[lambda x=x:x*10 for x in range(1,11)] 
# for t in tbl:
#     print(t())

maxim = lambda a, b: a if a > b else b  
# print(maxim(3, 5))

# message = lambda: print("hello") 
# message()
# message = lambda x: print(f'Hello {x}') 
# message('Miras')
# message = lambda x, y, z: print(f'Hello {x}, {y}, {z}') 
# message('Miras', 'Rasul', 'Asanali')
