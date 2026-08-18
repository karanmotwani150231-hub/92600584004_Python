list =[11,22,33,44,55,66,77,88,99]
print("Indexing :")
print("first element=",list[0])
print("second element=",list[-1])

print("slicing :")
print("first three elements",list[:3])
print("last three elements",list[-3:])
print("reverse list",list[::-1])

print("list manipulation :")
list.append(110)
print("after append=",list)
list.remove(22)
print("After remove=",list)


print("lidt comprehension :")
square=[x*x for x in list]
print("square list =",square)
