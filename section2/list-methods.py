# LIST METHODS IN PYTHON
numbers = [1,10, 5, 16 , 4, 9, 10]
letters = ["a","g","s","b","y","a","s"]

val = min(numbers)
val = max(numbers)

print(val)


numbers[4] = 25

#Eleman ekleme
numbers.append(96)
numbers.insert(3,78)

#Eleman silme
#numbers.pop()
# numbers.pop(1)
numbers.remove(9)

#Sıralama yapmak
numbers.sort()
letters.sort()

#Ters çevirmek
numbers.reverse()

#count metodu
print("10 sayısı kaç tane: " , numbers.count(10))
print(letters.count("a"))

#clear metodu ile tüm elemanlar silinir , numbers.clear()

print(numbers)
print(letters)


