"""
Yarıçapı verilen bir dairenin alan ve çevresini hesaplayınız
(p = 3.14)

alan = pr2
daire çevresi = 2pr

"""

radius = input ("Yaricapi giriniz : ")

r = float (radius)
pi = 3.14
alan = pi * ( r **2)
cevre = 2* pi * r

# print ("Daire alanı : " , alan)
# print ("Daire çevresi : " , cevre )

print ( "daire alanı : " + str(alan) + "daire cevresi : "  +str(cevre) )

