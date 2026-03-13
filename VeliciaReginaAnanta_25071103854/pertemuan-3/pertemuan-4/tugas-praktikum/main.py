from tabulate import tabulate
from kurs import kursUang
from konverter import IDR_ke_kurs_asing, kurs_asing_ke_IDR, asing_ke_asing

# TAMPILAN MENU
header = ['Kode', 'Kurs']
tampilkanKurs = [
   ['USD', kursUang["USD"]],
   ['EUR', kursUang["EUR"]],
   ['CNY', kursUang["CNY"]],
   ['JPY', kursUang["JPY"]],
   ['SGD', kursUang["SGD"]]
]
print('=== KONVERTER MATA UANG ===')
print(tabulate(tampilkanKurs, headers=header, tablefmt="fancy_grid"))


# INPUT
listKurs = kursUang.keys()
kursAsal = input("Dari (IDR\\USD\\EUR\\CNY\\JPY\\SGD): ")
kursHasil = input("Ke (IDR\\EUR\\USD\\CNY\\JPY\\SGD): ")
kursAsal = kursAsal.upper()
kursHasil = kursHasil.upper()

if kursAsal not in listKurs or kursHasil not in listKurs:
   print('Input tidak valid.')
   exit()

try:
   nominal = float(input("Nominal: "))
except ValueError:
   print('Nominal harus berupa angka.')
   exit()


# TUKAR KURS
if kursAsal == "IDR":
   hasil = IDR_ke_kurs_asing(nominal, kursHasil)
   print (f'\nRp {nominal} = {hasil:.2f} {kursHasil}')
elif kursHasil == "IDR":
   hasil = kurs_asing_ke_IDR(nominal, kursAsal)
   print (f'\n{nominal} {kursAsal} = Rp {hasil:.2f}')
else:
   hasil = asing_ke_asing(nominal, kursAsal, kursHasil)
   print (f'\n{nominal} {kursAsal} = {hasil:.2f} {kursHasil}')
