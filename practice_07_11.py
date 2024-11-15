import collections
import re

a = [2,1,3,4,5,6]
b = [1,4,5,7,8]

def is_increasing(x):
    return print(x==sorted(x))

# is_increasing(a)
# is_increasing(b) 

# ---------------------------------------------
lst = [1,2,1,3,2,3,2,3,2,2]
a = 3
k = 2

def kth_appearance(lst,a,k):
    counter=0
    for index, obj in enumerate(lst):
        if obj == a:
            counter+=1
        if counter == k:
            return index
    return -1

# print(kth_appearance(lst, a, k))

# -----------------------------------------------


def memoryAnalyzer(s, n, lst):
    lst = sorted(lst)
    if lst[0]>s:
        return 0
    
    for index, obj in enumerate(lst):
        if obj<s:
            s=s-obj
        else:
            return index
    return n

# print(memoryAnalyzer(400, 2, [200, 50, 200,100]))

# --------------------------------------------------
km = [10, 20 ,30]
cost = [50, 20, 30]

def taxiCost():
    global km, cost
    km = sorted(km)
    cost = sorted(cost, reverse=True)
    sum = 0
    for i in range(len(km)):
        sum = sum + km[i]*cost[i]
    return sum

# print(taxiCost())   

# --------------------------------------------------

def counter():
    lst = []
    while True:
        num = int(input())
        if num == 0:
            break
        lst.append(num)
    cnt = collections.Counter()
    for i in lst:
        cnt[i] +=1

    for i in range(1, 10):
        print(cnt[i], end=' ')


# counter()

# ----------------------------------------------
lst = [7,9,5,6,-99,-32,10,-6,45,14]

def finder(lst, k):
    for i, obj in enumerate(lst):
        if k == obj:
            return True, i
        
# print(finder(lst, -32))


# -----------------------------------

s = 'Hello world some word more!'

print(re.match('^[a-zA-Z0-9_.+-]*', s).group())

s = 'Hello 20-14-2025 some word more!'

print(re.match('[0-9]*-[0-9]*', s).group())




    
    
