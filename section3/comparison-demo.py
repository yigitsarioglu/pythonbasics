# 1- Girilen 2 sayıdan hangisi daha büyüktür

# a = int ( input ("Sayi giriniz : "))
# b= int ( input ("Sayi giriniz : "))

# if a >= b :
#     print("Büyük sayı: " ,a)
# else:
#     print("Büyük sayı: " ,b)


# 2- Kullanıcıdan 2 vize (%60) ve final notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın

vize1 = int( input("1.vize notunuz: "))
vize2 = int (input ("2.vize notunuz: "))
final = int (input("Final notu: "))

ortalama = (vize1*0.3) + (vize2*0.3) + (final*0.4)

print(f'not ortalamanız {ortalama}  ve dersten geçme durumunuz {ortalama >= 50} ')

# if ortalama >= 50 :
#     print ("Geçtiniz ", ortalama)
# else : 
#     print("Kaldınız" , ortalama)     


# 3 - Girilen bir sayının tek mi çift mi olduğunu yazdırın.

# sayi = int (input ("Sayi giriniz: "))
# if sayi%2 ==0 :
#     print("sayi çift sayidir")
# else:
#     print("tek sayi")


# 4 - Girilen bir sayınınn negatif pozitif durumunu yazdırın

# if sayi >=0 :
#     print("pozitif sayi ")
# else :
#     print ("negatif sayi")    


# 5 - Parola ve email bilgisini isteyip doğruluğunu kontrol edin
# (email : email@sadikturan.com parola : abc123)
email  ="email@sadikturan.com" 
parola = "abc123"

girilenMail = input ("Email adresiniz : ")
girilenParola = input ("Parolanız : ")

isEmail = (email == girilenMail.lower().strip() )
isParola = ( parola == girilenParola.lower().strip() )


print ( f'Mail adresi doğru mu {isEmail} , parola doğru mu {isParola}')

