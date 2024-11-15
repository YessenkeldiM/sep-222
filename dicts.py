# d = dict(1='dict', long='dictionary')

def helloWorld():
    print('Hello world')

d2 = {1:'dict', 'long':'dictionary'}
# print(d2)
v1 = (1, 1)
# print(type(v1))
d3 = dict([v1, (4,2), (2,4)])
# print(d3.setdefault(4, 500))
# print(d3)
d3.update([(7,9)])
d3.update({'hello': 'world'})
# print(d3)
d3['new kew'] = 5
# print(d3['key'])

# for key, value in d3.items():
#     print(key, value)

# for value in d3.values():
#     print(value)

# for key in d3.keys():
#     print(key)

users_list = [("+111123455", "Tom"),
 ["+384767557", "Bob"],
 ["+958758767", "Alice"]
 ]
users_dict = dict(users_list)
# print(users_dict)

