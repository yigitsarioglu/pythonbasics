# SETS
# listede aynı elemandan birden fazla bulunmaz


fruits = {'orange', 'banana', 'apple'}

# print(fruits[0])   **** set objeler indekslenemez

for x in fruits :
    print(x)


fruits.add("cherry") 
fruits.update ( ["mango", "grape"])

fruits.remove("mango")
fruits.discard("banana")
 # fruits.clear()
 # fruits.pop()
print(fruits)


myList= [1,2,5,5,5 ,3,3,4,4]
print(set(myList))