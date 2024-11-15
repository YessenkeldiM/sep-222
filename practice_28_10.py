#1
mylist = [1,2,3,4,5,6]
mydict = {}
for i in mylist:
    mydict[i] = i

# print(mydict)
#2
mystr = '123124632362352347879712315789322566'
mylist = list(mystr)
myset = set(mylist)  # сделать только уникальные значения
mydict = {}
for element in myset:
    mydict[element] = mylist.count(element)

resultdict = {}
vals = mydict.values()
vals = sorted(vals)
print(vals)
for key, valye in mydict.items():
    ...
print(mydict)