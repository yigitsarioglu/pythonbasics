#1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
# durumunu kontrol ediniz. Ehliyet alma koşulu en az  18  ve eğitim
# # durumu lise yada üniversite olmalıdır.

# isim = input ("İsminiz : ")
# yas = int ( input ("Yaşınız : ") )
# egitim = input ("Eğitim durumunuz : ")

# if  yas >= 18 :

#   if (egitim=="lise" or egitim == "universite") :
#     print (f"{isim} Ehliyet alabilirsin" )

#   else:
#     print (f"{isim} Ehliyet alamazsın, egitim durumun yetersiz. ")

# else:
#     print(f"{isim} Ehliyet alamazsın, yaşın tutmuyor.")    

    # 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
    # not aralığına karşılık gelen not bilgisiniz yazdırınız.
    # 0-24 => 0
    # 25 -44 => 1
    # 45-54 =>2
    # 55-69 =>3
    # 70 -84=>4
    # 85-100=>5

# sinav1 = float ( input("1. Yazılı sınav sonucu : "))
# sinav2 = float ( input("2. Yazılı sınav sonucu : "))
# sozlu = float ( input("Sözlü sınav sonucu : "))

# ortalama = (sinav1 + sinav2 + sozlu ) /3

# if ortalama>=0 and ortalama<25 :
#     print(f"notunuz 0 , ortalamanız : {ortalama}")
# elif ortalama>=25 and ortalama<45 :
#     print(f"notunuz 1 , ortalamanız : {ortalama} ")    
# elif ortalama>=45 and ortalama<55 :
#     print(f"notunuz 2 , ortalamanız : {ortalama}")
# elif ortalama>=55 and ortalama<70 :
#     print(f"notunuz 3 , ortalamanız : {ortalama} ")           
# elif ortalama>=70 and ortalama<85 :
#     print(f"notunuz 4 , ortalamanız : {ortalama}")         
# elif ortalama>=85 and ortalama<=100 :
#     print(f"notunuz 5 , ortalamanız : {ortalama} ")       
# else : 
#     print ("yanlış bilgi girdiniz...")     


# 3 - Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
# 1.Bakım  => 1.yıl
# 2.Bakım => 2.yıl
# 3. Bakım => 3.yıl
# Süre hesabını alınan gün,ay,yıl bilgisine göre gün bazlı hesaplayınız
# **datetime modülünü kullanmanız gerekiyor.

# days = int (input("aracınız kaç gündür trafikte: " ))

# if days<=365 :
#     print (" 1.servis aralığı")
# elif days>365 and days <= 365*2 :
#     print ("2.servis aralığı")
# elif days>365*2 and days<=365*3 :
#     print (" 3.servis aralığı ")
# else : 
#     print ("hatalı süre... ")        

import datetime


tarih = input ("Aracınız hangi tarihte trafiğe çıktı (yıl/ay/gün) : ")

tarih = tarih.split('/')



trafigeCikis = datetime.datetime( int( tarih[0]) ,int( tarih[1]) , int( tarih[2])  )
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

print ("Gün olarak Gecen zaman :   ", fark.days )

if days<=365 :
    print (" 1.servis aralığı")
elif days>365 and days <= 365*2 :
    print ("2.servis aralığı")
elif days>365*2 and days<=365*3 :
    print (" 3.servis aralığı ")
else : 
    print ("hatalı süre... ")     


