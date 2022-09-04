# key -value

# sehirler = [ "kocaeli" , "istanbul"]
# plakalar = [41 , 34]

# print( plakalar[ sehirler.index("kocaeli")] )
# print( plakalar[ sehirler.index("istanbul")] )


#DICTIONARY
# plakalar = { "key " : " value" } 

# plakalar = {"istanbul": 34, "kocaeli":41}
# print(plakalar["istanbul"])


# plakalar["ankara"] = 6
# plakalar["kocaeli"] = "new value"
# print(plakalar)


users = {
    'sadikturan': {
        'age':20,
        'roles' : ['user'],
        'email' :"sadikturan@gmail.com",
        'telefon':5553336688,
        'adress':"Kocaeli"
    },

    'cinarturan':{
        'age':45,
        'roles' : ['user','admin'],
        'email' :"cinar@gmail.com",
        'telefon':22535885,
        'adress':"Bursa"
    }

}

print(users['cinarturan']) 
print(users['cinarturan']["age"])
print(users['cinarturan']["roles"][1])