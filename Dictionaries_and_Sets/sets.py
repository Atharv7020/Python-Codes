a={1,3,6,7,8,6}
print(type(a))
print(a)   #does not print repetitive items
b=set()             #empty set
print(type(b))
#print(b)

b.add(4)
b.add(5)
b.add(7)
b.add(2)
b.add(1)
b.add(1)
print(b)

b.remove(2)
print(b)

b.clear()
print(b)