class Mahasiswa:
   def __init__(self, nama, nim, kelas):
      self.nama = nama
      self.nim = nim
      self.kelas = kelas

   def memperkenalkan_diri (self, nama, nim):
      print (f'Haloo nama saya {nama} dengan nim {nim}')

   def update_nim (self, new_nim):
      self.nim = new_nim

mhs1 = Mahasiswa("Velicia", "25071100000", "TI C")
mhs2 = Mahasiswa("Putri", '25071100001', 'TI B')
mhs3 = Mahasiswa("Putra",'25071100002', "TI A")

mhs1.update_nim("2502333333")


