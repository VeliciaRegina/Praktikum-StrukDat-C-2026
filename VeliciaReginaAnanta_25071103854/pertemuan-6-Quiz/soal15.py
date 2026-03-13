import soal11
import soal12
import soal13
import soal14

menu = """=== PyGadget Hub === 
1. Tambah Gadget 
2. Daftar Inventaris 
3. Update Stok 
4. Cek Komisi 
5. Keluar """

print(menu)
menu = int(input('Pilih menu: '))
while menu != 5:
   match menu:
      case 1: soal11.registrasi_gadget()
      case 2: soal12.stok_gadget()
      case 3: soal13.update_stokk()
      case 4: soal14.hitung_komisi()
      case 5: print('Menghentikan program'), exit()