name = "yigit"
surname = "sarioglu"
age = 33

greeting = "my name is " + name + " surname is " + surname + " and \nI am " + str(age) + " years old"

length = len(greeting)


print(greeting)
print(greeting[0:3])
# print( greeting[length -1]  )
# print( greeting[-1])

print ( greeting[3:15])
print ( greeting[3:30:2])