# Set digunakan untuk menyimpan banyak item dalam satu variabel.
# Item di set tidak terurut, tidak dapat diubah, dan tidak mengizinkan duplikat

"""                        
add()		                                    Menambahkan elemen ke set
clear()		                                 Menghapus semua elemen dari set
copy()		                                 Mengembalikan salinan set
difference()              	         -	      Mengembalikan set yang berisi selisih antara dua set
difference_update()	               -=	      Menghapus item dalam set ini yang juga termasuk dalam set lain yang ditentukan
discard()		                              Menghapus item yang ditentukan
intersection()	                     &	      Mengembalikan set yang merupakan irisan dari dua set lain
intersection_update()	            &=	      Menghapus item dalam set ini yang tidak ada dalam set lain yang ditentukan
isdisjoint()		                           Mengembalikan apakah dua set memiliki irisan atau tidak
issubset()	                        <=       Mengembalikan True jika semua item dari set ini ada dalam set lain
	                                 <	      Mengembalikan True jika semua item dari set ini ada dalam set lain yang lebih besar
issuperset()	                     >=	      Mengembalikan True jika semua item dari set lain ada dalam set ini
	                                 >	      Mengembalikan True jika semua item dari set lain yang lebih kecil ada dalam set ini
pop()		                                    Menghapus elemen dari set
remove()		                                 Menghapus elemen yang ditentukan
symmetric_difference()	            ^	      Mengembalikan set dengan selisih simetris dari dua set
symmetric_difference_update()	      ^=	      Memasukkan selisih simetris dari set ini dan set lain
union()	                           |	      Mengembalikan set yang berisi gabungan dari set
update()	                           |=	      Perbarui set dengan gabungan set ini dan set lainnya
"""

set1 = {"abc", 34, True, 40, "male"}
print(set1)

# True dan 1 dianggap sama. False dan 0 dianggap sama
thisset = {"apple", 1, "banana", "cherry", False, True, 0}
print(thisset)

# Mengetahui panjang set menggunakan len()
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Tipe set
myset = {"apple", "banana", "cherry"}
print(type(myset))

# Konstruktor set()
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


# MENGAKSES ITEM SET
# Menggunakan loop for
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
      
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)


# MENAMBAHKAN ITEM SET
# Method add() menambahkan item ke akhir set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Method update() menambah item dari satu set ke set lain
# Dapat berupa tuple, set, dictionary
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


# MENGHAPUS ITEM SET
# Method remove() 
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Method discard()
# Jika item tidak ada, disccard() tidak menampilkan error
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# Method pop() menghapus item random
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#Method clear() mengosongkan set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# Kata kunci del menghapus set sepenuhnya
thisset = {"apple", "banana", "cherry"}
del thisset


# LOOP SET
# Loop for
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


# MENGGABUNGKAN SET
# Method union() mengembalikan set baru berisi semua item dari kedua set
# memperbolehkan menggabungkan dnegan set atau tuple
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# Method update() menambahkan item dari satu set ke set lainnya
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Method intersection() mengembalikan set baru berisi item yang terdapat di kedua set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# Method intersection_update() hanya menyimpan duplikat, akan mengubah original set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# Method difference() mengembalikan set baru berisi item yang ada di set pertama tetapi tidak ada i set kedua
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

# Method difference_update()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

# Method symmetric_difference() hanya menyimpan item yang tidak ada di kedua set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

# Method symmetric_difference_update()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)


# FROZENSET
# Set yang tidak dapat diubah
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

