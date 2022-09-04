x, y,z = 2,5,10

numbers = 1, 5 , 7 ,10







# 1 - Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
# deger1 = input( "ilk sayı: ")
# deger2 = input ("ikinci sayi : ")

# carpim = int(deger1) * int(deger2)

# result= carpim - (x+y+z)
# print (result)


# 2 - y'nin x' e kalansız bölümünü hesaplayınız.

print( "y nin x'e kalansız böümü: " , y//x)

# 3- (x,y,z) toplamının mod 3 'ü nedir?

print ( " (x,y,z) toplamının mod 3 : "  , ( (x+y+z)%3) )



# 4 - y' nin x kuvvetini hesaplayınız.

print ( " y' nin x kuvveti : " ,  ( y**x) )




# 5 -  x, *y ,z = numbers  işlemine göre z'nin küpü kaçtır?

x, *y,z = numbers
print (" z nin küpü : " , (z**3))


# 6 - x,*y,z =numbers işlemine göre y'nin değerleri toplamı kaçtır?

res= y[0] + y[1] 

print( res)

