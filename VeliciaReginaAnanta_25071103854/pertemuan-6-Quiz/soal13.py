katalog = [ 
   {'merk': 'Samsung', 
    'tipe': 'S23', 
    'sn': 'SAM01', 
    'stok': 2}, 

    {'merk': 'Oppo', 
     'tipe': 'Reno 10', 
     'sn': 'OPP01', 
     'stok': 5} ] 

daftar_merk = set()
def update_stokk(katalog, sn_target, jumlah_tambah):
   for x in katalog:
      if x['sn'] == sn_target.upper():
         x['stok'] += jumlah_tambah


for x in range (3):
   sn_target = input('Masukkan SN: ')
   jumlah_tambah = int(input('Masukkan jumlah stok yang ingin ditambah: '))

   p = update_stokk(katalog, sn_target, jumlah_tambah)
   print(f'Updat berhasil. stok {katalog[x]['merk']} sekarang: {katalog[x]['stok']}')
   print(x["merk"])

   