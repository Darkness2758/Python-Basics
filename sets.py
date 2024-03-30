a1 = {2,3,4,5,6,7,77,7,7,8}
a2 = {3,4,5,6,76,678}

print(a1) #one element prints one time
print(a2)

#exploration
print(a1.difference(a2))
print(a1.intersection(a2))
print(a1.union(a2))
print(a1.isdisjoint(a2))


#How to Make a Empty Set ?
null = set()
print("This is a empty set :" , null)