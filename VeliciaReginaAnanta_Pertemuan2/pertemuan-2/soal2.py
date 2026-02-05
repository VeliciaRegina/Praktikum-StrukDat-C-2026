barang = ("B001", "Laptop Gaming", 15000000)

print (f'Harga barang: {barang[2]}')

barang[2] = 14000000
# terjadi error karena sifat dari tuple tidak bisa diubah (unchangeable), jika ingin mengubah elemen/value, harus mengubah tuple tersebut ke dalam bentuk list

barang = ("B001", "Laptop Gaming", 15000000)
(kode, nama, harga) = barang
print (kode)
print (nama)
print (harga)