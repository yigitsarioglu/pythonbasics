# 1 - Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# sayi1 = int ( input ("Bir sayi giriniz: "))

# result = (sayi1 >0 ) and  (sayi1 <=100)
# print (f'girilen sayi 0-100 arasındamı {result} ')

# # 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# pozcift = (sayi1 % 2==0 ) and (sayi1>0)
# print (f'girilen sayi pozitif ve çift :  {pozcift}')

# # 3 - Email ve parola bilgileri ile giriş kontrolü yapınız.
# email = 'email@sadikturan.com'
# password = 'abc123'

# girilenMail = input("Email giriniz: ")
# girilenPassword = input ("Parola giriniz : ")

# kontrol = (girilenMail==email) and (girilenPassword==password)
# print(f'uygulamaya giris başarılı mı:  {kontrol}')

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız

# a = int( input(" a : "))
# b = int( input(" b: "))
# c = int( input(" c: "))

# ress = (a>b) and (b>c)
# print(f' a en büyük sayidir {ress}')
# ress = (b>a) and (b>c)
# print(f' b en büyük sayidir {ress}')
# ress = (c>b) and (c>a)
# print(f' c en büyük sayidir {ress}')

# 5 - Kullanıcıdan 2 vize(%60 ) ve final (%40) notunu alıp ortalama hesaplayınız.
#Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
# a) ortalama 50 olsa bile final notu en az 50 olmalıdır
# b) finalden 70 alındığında ortalamanın önemi olmasın

# vize1 = int( input(" 1.vize notu : "))
# vize2 = int( input(" 2.vize notu :"))
# finalnot = int( input(" final notu :"))

# ortalama = ( (vize1+vize2) /2 )*0.6 + finalnot*0.4

# gecernot = ( (ortalama>=50) and (finalnot>=50) ) or (finalnot >=70)
# print (f"ogrenci gecer mi : {gecernot} , ortalaması {ortalama}")

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
# Formül : (Kilo/boy uzunluğunun karesi)
# Aşağıfaki tabloya göre kişi hangi gruba girmektedir
# 0-18.4 => zayıf
# 18.5 - 24.9 => normal
# 25.0-29.9 => fazla kilolu
# 30.0 - 34.9 => şişman(obez)

ad = input ("adiniz : ")
kilo = float ( input ("kilonuz: "))
boy = float ( input( "boyunuz: "))
boy = boy*0.01

indeks = ( kilo / (boy**2) )
sonuc = (indeks>0) and (indeks<18.4)
print ( f"zayif mi:  {sonuc}, endeks {indeks} ")

sonuc = (indeks>18.5) and (indeks<24.9)
print ( f"normal :  {sonuc} , endeks {indeks}  ")

sonuc = (indeks>25.0) and (indeks<29.9)
print ( f"fazla kilolu :  {sonuc} , endeks {indeks}  ")

sonuc = (indeks>30.0) and (indeks<34.9)
print ( f"şişman :  {sonuc} , endeks {indeks}  ")

sonuc = (indeks>35.0) 
print ( f"morbid obez:  {sonuc} , endeks {indeks}  ")