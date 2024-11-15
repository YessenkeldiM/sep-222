
####### BANK
# x = 1
# money = 1000
# while int(x) != 0:
#     print("***USERNAME***\n1. Check balance\n2. Withdraw\n3. Deposit\n0. Exit")
#     x = int(input())
#     if x == 0:
#         break
#     if x == 1:
#         print("Your balance: " + str(money) + "$")
#     if x == 2:
#         asdf = int(input("How many you want to withdraw: "))
#         money -= asdf
#     if x == 3:
#         asdf = int(input("How many you want to deposit: "))
#         money += asdf

###### Recursive POWER
def power(z, p):
    if p == 0:
        return 1
    return (z*power(z, p-1))
 
print("Here we counting power of a number - ")
z = int(input("Please enter number: "))
p = int(input("Please enter power: "))
print(power(z, p))

###### Factorial
y = input("Please, enter number - ")
def factorial(num):
    ret = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            ret = ret * i
    print("The factorial of", num, "is", ret)

factorial(int(y))

###### Fibbonicci

def fibfib(k):
   if k <= 1:
       return k
   else:
       return(fibfib(k-1) + fibfib(k-2))

w = 9
while int(w) > 0:
    print(str(w) + " - " + str(fibfib(w)))
    w -= 1

####### SuM
def sumsum(f, g):
    if f == g: return g
    else: return f + sumsum(f + 1, g)

r = 3
t = 5
print("from "+ str(r) + " to " + str(t) + " is ")
print(sumsum(r, t))

'''
add_three_calls = 0
def add_three(number):
    global add_three_calls
    print(f'Returning {number + 3}')
    add_three_calls += 1
    return number + 3

a = 3
v = add_three(a)
print(v)
print(add_three_calls)

'''