sayilar = [1,3,5,7,9,12,19,21]

# 1 -Sayiler listesindeki hangi sayılar 3'ün katıdır?

for sayi in sayilar:
    if sayi%3 ==0 : 
        print(f'{sayi} 3 ün katıdır')

 # 2 -Sayilar listesindeki sayilarin toplami nedir?

toplam=0
for sayi in sayilar:
    toplam+=sayi

print(f"toplam sayi : {toplam}")    

# 3 - Sayılar listesindeki tek sayıların karesini alınız.

for sayi in sayilar :

    if sayi %2 ==1 :
        karesi = sayi**2
        print(f' {sayi} karesi {karesi}')

sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir' , 'rize']

# 4 - Şehirlerden  hangileri en fazla 5 karakterlidir?

for sehir in sehirler :
    if len(sehir) <=5 :
        print(sehir)


urunler = [
    { 'name' : 'samsung S6', 'price': '3000'},
    {'name' : 'samsung s7' , 'price' : '4000'},
     {'name' : 'samsung s8' , 'price' : '5000'},
     { 'name' : 'samsung s9' , 'price' : '6000' },
      { 'name' : 'samsung s10' , 'price' : '7000' }
]

# 5 - Ürünlerin fiyatları toplamı nedir?
toplam_fiyat=0

for urun in urunler :
    toplam_fiyat += int( urun['price'] )
    print (urun['price'])

print("toplam fiyat ", toplam_fiyat)

# 6 - Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz?

for urun in urunler:

    if ( int(urun['price']) <= 5000 ) :
        print(urun['name'])
