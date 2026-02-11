# Tuple digunakan untuk menyimpan beberapa item dalam satu variabel.
# Item di tuple terurut, tidak dapat diubah, dan mengizinkan duplikat

"""
count()  	Mengembalikan jumlah kemunculan nilai tertentu dalam sebuah tuple.
indeks()	   Mencari nilai tertentu dalam tuple dan mengembalikan posisi di mana nilai tersebut ditemukan.
"""


tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# Mengetahui panjang tuple menggunakna len()
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Membuat tuple dengan saru item, gunakan koma setelah item
thistuple = ("apple",)
print(type(thistuple))

# Tipe data tuple
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# Konstruktor tuple()
thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)


# MENGAKSES ITEM TUPLE
# Mengakses item tuple melalui indeksnya
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negatif indeks berarti mulai dari urutan terakhir
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Menentukan rentang spesifik dari item tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Rentang dengan indeks negatif
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Mengecek jika item ada
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


# UPDATE TUPLES
# Mengubah tuplle ke list, kemudian mengubahnya lagi ke tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Menambahkan tuple ke tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# Menghapus item
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
del thistuple


# UNPACK TUPLE
# Mengekstrak values ke dalam variabel
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


# LOOP TUPLE
# Gunakan loop for
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Loop melalui indeksnya menggunkan range() dan len()
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Whle loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


# MENGGABUNGKAN TUPLE
# Menggunakan operator +
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Mengalikan tuple menggunakan *
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

