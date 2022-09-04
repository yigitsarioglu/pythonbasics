# IDENTITY AND MEMBERSHİP OPERATORS
# IS VE IN OPERATÖRLERİ

# Identity Operator : is

# x = y = [1,2,3]
# z = [1,2,3]

# print (x==y)   # value type
# print (x == z)

# print (x is y) # reference type
# print (x is z)


from telnetlib import NAOCRD


x = [1,2,3]
y= [2,4]

del x[2]
y[1]=1
y.reverse()

print (x==y)
print (x is y)
print (x is not y)


#Membershi Operator : in

m = ["apple", "banana"]

print ("banana" in m)

name = 'Çınar'

print ('a' in name)
print ('b' not in name)