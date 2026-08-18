print ("tupple :")
digits = (1,20,30,40,50)

print("tupple :",digits)
print ("first element :",digits[0])
print ("last element :",digits[-1])

print("first three elements :",digits[:3])
print("length of tupple :",len(digits))
print("count of 20 :",digits.count(20))
print("count of 30 :",digits.count(30))

set1={10,20,30,40,50}
set2={40,50,60,70,80}

print("\n set1 :",set1)
print("\n set2 :",set2)
print("union :",set1.union(set2))
print("intersection :",set1.difference(set2))
print("difference (set1 -set2) :",set1.difference(set2))
print("symmetric difference :",set1.symmetric_diffference(set2))

set1.add(90)
print("after ading 90 :",set1)

set1.remove(20)
print("after removing :",set1)

      
