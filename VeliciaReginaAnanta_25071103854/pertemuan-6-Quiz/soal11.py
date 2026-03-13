def registrasi_gadget(merk, tipe, harga, sn):
   if harga < 1_000_000:
      print('Harga harus berupa angka')
      return None
   if len(sn) < 5:
      print('SN harus harus memuat minimal 5 karakter')
      return None
   
   dict1 = {'merk': merk, 'tipe': tipe, 'harga': harga, 'sn': sn, 'status': 'tersedia'}
   return dict1

list_inventaris =[]
for x in range (3):
   merk = input('Masukkan merk: ')
   tipe = input('Masukkan tipe: ')
   harga= float(input('Masukkan harga: '))
   sn = input('Masukkan SN: ')

   p = registrasi_gadget(merk, tipe, harga, sn)
   list_inventaris.append(p)


for x in list_inventaris:
   print(x)