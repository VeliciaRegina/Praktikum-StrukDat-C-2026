stok_barang = [15, 40, 30, 10, 25]

stok_barang[3] = 50

stok_barang.append(5)
stok_barang.sort(reverse=True)
print(stok_barang)

jumlah = sum(stok_barang)
print (jumlah)

avg = jumlah/len(stok_barang)
stok_aman = ("aman" if avg > 20 else "waspada")
print(stok_aman)