website = "http://www.sadikturan.com"

course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin?
hello = " Hello World "
hello = hello.strip()
print(hello)

# 2- 'www.sadikturan.com' içindeki sadıkturan bilgisi haricindeki her karakteri silin.
mes ='www.sadikturan.com'
mes = mes.split(".")

#print(mes[1])

result = 'www.sadikturan.com'.strip("w.moc")
print(result)

# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

courselower= course.lower()
#course = course.upper()
#course = course.title()
print(courselower)


# 4- 'website' içinde kaç tane a karakteri vardır? (count('a'))

res = website.count("a")
print(res)



# 5- 'website' 'www' ile başlayıp com ile bitiyor mu?
isFoundw = website.startswith("www")
isFoundc = website.endswith("com")
print("website startwith www: " ,isFoundw)
print("website endswith com: " ,isFoundc)

# 6- 'website' içinde '.com' ifadesi var mı?

isFoundcom = website.find(".com")
print("website contains .com " ,isFoundcom)

ress= website.find("com", 0 ,20)
ress= website.index("com")
ress= website.rindex("com")
print(ress)

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha,isdigit)

alphas= course.isalpha()
print(alphas)

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz?
con= "Contents".center(50,"*")
# con = "Contents".ljust(50,"*")
# con = "Contents".rjust(50,"*")
print(con)


# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştirin.

c = course.replace(" ", "-")
# c = course.replace(" ", "")
print(c)

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' ile değiştirin.

hel = "Hello World".replace("World", "There")
print(hel)

# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın.

cors = course.split()
print(cors)