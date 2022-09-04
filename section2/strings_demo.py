website = "http://www.sadikturan.com"

course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır?
length_course = len(course)
print(length_course)

# 2 - 'website' içinden www karakterlerini alın.
length_website=len(website)

# x = website[0:7]
# y= website[10:]
#  print(x+y)

w = website[7:10]
print(w)

# 3 - 'website' içinden com karakterlerini alın.


# web = website[0:length_website -3]
# print(web)
u = website [length_website-3 : ]
print (u)

# 4 - 'course' içinden ilk 15 ve son 15 karakterlerini alın.
first15= course[0:15] # course[:15]
last15 = course [-15 : ]
print(first15 + ' ' + last15)



# 5 - 'course' ifadesindeki karakterleri tersten yazdırın.
res = course[::-1]
print(res)




name, surname,age,job = 'Bora','Yılmaz', 32 , 'mühendis'
# 6 - Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis'

print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}")


# 7 - 'Hello world' ifadesindeki w harfini W ile değiştirin.
hello = "Hello world"
# print( hello[6] )
hellos = hello[0:6] + 'W' + hello[-4:]
print(hellos)

# 8 - 'abc' ifadesini yan yana 3 defa yazdırın
abc= "abc "
print( abc*3)