skema_komisi = ( 
(100000000, 10), # Penjualan >= 100jt -> Komisi 10% 
(50000000,  5),  # Penjualan >= 50jt  -> Komisi 5% 
(20000000,  2),  # Penjualan >= 20jt  -> Komisi 2% 
(0,         0)   # Di bawah 20jt      
) 

def hitung_komisi(total_penjualan, skema, index=0):
   for x in skema_komisi:
      if total_penjualan >= skema_komisi[index][0]:
         return x[1]/100
      elif total_penjualan < skema_komisi[0]:
         index += 1
         hitung_komisi(total_penjualan, skema, index)

      
nama = input('Nama sales: ')
totalJual = int(input('Total penjualan: '))
totalKomisi = totalJual * hitung_komisi(totalJual, skema_komisi, index =0)

print(f'Nama {nama} memiliki komisi {totalKomisi}')