stok = [15, 50, 30, 25, 40]

stok.append(100)
print(stok)

stok.insert(1, 75)
print(stok)

stok.sort()
print(stok)

jumlah = 0
for x in range(len(stok)):
   jumlah += stok[x]
   avg = jumlah /(x+1)

print(f"Rata-rata: {avg}")

print(stok)
