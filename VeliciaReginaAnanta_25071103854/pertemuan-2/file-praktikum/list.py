# List digunakan untuk menyimpan banyak item dalam satu variabel.
# Item di list terurut, dapat diubah, dan mengizinkan duplikat

"""
append() 	Menambahkan elemen di akhir list
clear()  	Menghapus semua elemen dari list
copy()	   Mengembalikan salinan list
count()  	Mengembalikan jumlah elemen dengan nilai yang ditentukan
extend()    Menambahkan elemen dari list (atau iterable apa pun) ke akhir list saat ini
index()     Mengembalikan indeks elemen pertama dengan nilai yang ditentukan
insert()    Menambahkan elemen pada posisi yang ditentukan
pop()       Menghapus elemen pada posisi yang ditentukan
remove()    Menghapus item dengan nilai yang ditentukan
reverse()   Membalik urutan list
sort()      Mengurutkan list
"""


list1 = ["abc", 34, True, 40, "male"]
print(list)

# Menentukan panjang list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Tipe data list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))


#  MENGAKSES ITEM  DI LIST
# Mengakses item list melalui indeksnya
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negatif indeks berarti mulai dari urutan terakhir
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Menentukan rentang spesifik dari list item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Meninggalkan nilai awal, rentang akan memulai dari item pertama
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# Meninggalkan nilai akhir, rentang akan terus menelusuri hingga akhir list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Menentukan negatif indeks jika ingin memulai pencarian dari akhir list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# ek jika item ada dalam list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# MENGUBAH LIST ITEM
# Untuk mengubah nilai item tertentu, lihat nomor indeksnya
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Mengubah irem dengan rentang tertentu
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# Menyisipkan dengan method insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


# MENAMBAH LIST ITEM
# Menambahkan item ke akhir list, gunakan method append()
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Menambahkan item ke posisi tertentu, gunakan method insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Menambahkan elemen dari daftar lain ke daftar saat ini, gunakan method extend()
# Dapat berupa tuple, set, dictionary
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# MENGAPUS LIST ITEM 
# Menghapuus item terntu, gunakan method remove()
# Hanya menghapus yang pertama kali muncul
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Menghapus indeks tertentu gunakan method pop()
# Jika tidak menentukan indeks, pop() akan menghapus elemen terakhir
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# Kata kunci del menghapus spesifik indeks
# Dapat menghapus list sepenuhnya
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

# Mengosongkan list gunkaan method clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


# PERULANGAN LIST
# Loop for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Loop dengan nomor indeks menggunakan range() dan len()
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# Loop while
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Loop list comphrehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


# LIST COMPREHENSION
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

"""newlist = [expression for item in iterable if condition == True]"""


# SORT LIST
# Method sort() mengurutkan list secara alfanumerik
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Mengurutkan secara menurun gunakan reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Pengurutan tidak memakai huruf besar dan huruf kecil
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Method reverse() membalik urutan pengurutan elemen saat ini
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


# MENYALIN LIST
# Method copy() untuk menyalin list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Method list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Menggunakan operator slice (:)
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


# MENGGABUNGKAN DUA LIST
# Menggunakan operator +
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Menggunakan append()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

# Menggunakan extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)