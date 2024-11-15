import itertools

g = (x**2 for x in itertools.count(2, 2))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
