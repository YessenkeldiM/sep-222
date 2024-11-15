words = ["one", "two", "one", "three", "one"]
# print(set(words))

a = (2)
print(type(a))
# import copy
# first_element = [0]
# second_element = [1]
# print(id(first_element))
# print(id(second_element))
# c = [[0, 1], [1]]

# print(c[0][1])

# # b = copy.deepcopy(c)

# # Добавление и удаление в конце строки
# c.append('asasd')
# c.pop()

# # Добавление и удаление по индексу
# c.insert(0, 'abc')
# c.pop(0)

# # print(c)

# v = "h3110 23 cat 444.4 rabbit 11 2 dog"

# a = [s for s in v if not s.isdigit()]
# b = [s for s in v if s.isdigit()]
# # print(a, b)

# # print(v[::])
# # print(c[::-1])

countries = set()
while True:
    operation = input('Введите операцию')
    if operation == 'add':
        сountry = input('Введите страну')
        countries.add(сountry)
    elif operation == 'delete':
        сountry = input('Введите страну')
        countries.discard(сountry)
    elif operation == 'find':
        сountry = input('Введите страну')
        print(countries[сountry])