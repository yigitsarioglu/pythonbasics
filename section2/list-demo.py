# 1- "Bmw, Mercede, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
# 2- Liste kaç elemanlıdır?
# 3- Listenin ilk ve son elemanı nedir?
# 4- Mazda değerini Toyota ile değiştirin.
# 5- Mercedes listenin bir elemanı mıdır?
# 6- Listenin -2 indeksindeki değer nedir?
# 7- Listenin ilk 3 elemanını alın.
# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
# 10- Listenin son elemanını silin
# 11- Liste elemanlarını tersten yazdırın.

#answer 1
listem = ["Bmw", "Mercedes", "Opel" ,"Mazda"]

#answer 2
print("Liste uzunluğu: ",len(listem) )

#answer 3
print("listenin ilk elemanı: " , listem[0])
print("listenin son elemanı: ", listem[-1])

# answer 4
listem[-1]="Toyota"

print(listem)

# answer 5
if "Mercedes" in listem:
    print("yes mercedes is in the list")

#answer 6
print("listenin -2 indeksindeki değer: ", listem[-2])

#answer 7
araba = listem[0:3]
print("ilk 3 eleman ", araba)

#answer 8
listem[-2:] = ["Toyota","Renault"]

print(listem)


#answer 9
listem.append("Audi")
listem.append("Nissan")
print(listem)

arabalar = listem + ["Audi", "Nissan"]



#answer 10
# del listem[-1]
listem.pop(-1)
print(listem)


#answer 11
ressult = listem[::-1]
print("tersten : " ,ressult)