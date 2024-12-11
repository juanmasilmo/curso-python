a = [1,2,3,4,5,6]
b = a

print(a)
print(b)
#del a[0]
print(a)
print(b)
print(id(a))
print(id(b))

c = a[:]

print(c)
print(id(c))