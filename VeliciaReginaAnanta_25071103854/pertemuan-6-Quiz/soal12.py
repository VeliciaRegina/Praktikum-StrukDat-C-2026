stok_gadget = [ 
{'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000}, 
{'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000}, 
{'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000}, 
{'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000}, 
]


def filter_harga(min_harga, max_harga):
   listGadget = []

   for x in stok_gadget:
      if min_harga < x['harga'] <= max_harga:
         listGadget.append(x['merk'])

   return listGadget


min_budget = float(input('Budget minimal: '))
max_budget = float(input('Budget maksimal: '))

daftar_merk = filter_harga(min_budget, max_budget)
print(f'Menampilkan gadget dengan harga {min_budget} - {max_budget}:')
print(daftar_merk)