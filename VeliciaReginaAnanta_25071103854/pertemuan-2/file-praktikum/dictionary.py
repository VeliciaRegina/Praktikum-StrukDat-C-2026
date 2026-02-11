# Dictionary digunakan untuk menyimpan banyak item dalam satu variabel.
# Dictionary terurut, dapat diubah, dan tidak mengizinkan duplikat
# Dictionary memiliki keys dan values

"""
clear()	      Menghapus semua elemen dari dictionaries
copy()	      Mengembalikan salinan dictionaries
fromkeys()	   Mengembalikan dictionaries dengan kunci dan nilai yang ditentukan
get()	         Mengembalikan nilai dari kunci yang ditentukan
items()	      Mengembalikan daftar yang berisi tuple untuk setiap pasangan kunci-nilai
keys()	      Mengembalikan daftar yang berisi kunci-kunci dictionaries
pop()	         Menghapus elemen dengan kunci yang ditentukan
popitem()	   Menghapus pasangan kunci-nilai yang terakhir dimasukkan
setdefault()	Mengembalikan nilai dari kunci yang ditentukan. Jika kunci tidak ada: masukkan kunci, dengan nilai yang ditentukan
update()	      Memperbarui dictionaries dengan pasangan kunci-nilai yang ditentukan
values()	      Mengembalikan daftar semua nilai dalam dictionaries
"""


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


# Mengetahui panjang dictionary menggunakan len()
print(len(thisdict))


# Tipe dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))


# dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)



# MENGAKSES ITEM
# Mengacu pada nama kunci dalam kurung suku
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


# Method get()
x = thisdict.get("model")
print(x)


# Method keys() mengembalikan semua kunci dalam bentuk list
x = thisdict.keys()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change


# Method values() mengembalikan semua nilai dalam dictionary
x = thisdict.values()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change


# Method items() mengembalikan setiap item, sebagai tuple dalam list
x = thisdict.items()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change


# Mengecek apakah kunci ada
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")


# MENGUBAH ITEM DICTIONARY
# Mengubah value item tertentu dengan mengacu ke nama kunci
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# Method update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


# MENAMBAH ITEM 
# Menggunakan indeks baru dan assign value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Method update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})


# MENGHAPUS ITEM
# Method pop() menghapus item dengan kunci spesifik
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# Method popitem() menghapus item terakhir
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# Kata kunci del
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# Method clear()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)


# LOOP DICTIONARY
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)


# MENYALIN DICTIONARY
# Menggunakan copy() dan dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)


# NESTED DIOTIONARIES
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}


# Mengakses item
print(myfamily["child2"]["name"])

# Loop melalui nested dictionaries
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])