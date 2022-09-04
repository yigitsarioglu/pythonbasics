


names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998,2000,1998,1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
print(names)

# 2- "Sena" değerini listenin başına ekleyiniz.
names.insert(0,"Sena")
print(names)

# 3- "Deniz" ismini listeden siliniz.
# names.remove("Deniz")
# print(names)

# 4- "Deniz" isminin indeksi nedir?
indis = names.index("Deniz")
print("Deniz isminin indeksi", indis)

# 5- "Ali" listenin bir elemanı mıdır?
eleman = "Ali" in names
print(eleman)

# 6- Liste elemanlarını ters çevirin.

#names.reverse()
# print(names)

print(names[::-1])

# 7- Liste elemanlarını alfabetik olarak sıralayın.
names.sort()
print(names)

# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)

# 9- str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
result = str.split(',')
print(result)


# 10- years dizisinin en büyük ve en küçük elemanı nedir?

maxElem = max(years)
minElem = min(years)
print( f"max element {maxElem} , min element {minElem}" )

# 11- years dizisinde kaç tane 1998 değeri vardır?

nums = years.count(1998)
print("years dizisinde kaç tane 1998 değeri : " , nums)

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
print("years listesi: " ,years)

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

# a = input("Marka 1 : ")
# b= input("Marka 2 : ")
# c = input("Marka 3 : ")
# markalistesi = []
# markalistesi = markalistesi + [a,b,c]
# print(markalistesi)