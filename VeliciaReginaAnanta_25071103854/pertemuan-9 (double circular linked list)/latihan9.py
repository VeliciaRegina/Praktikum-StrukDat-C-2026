class Node:
   def __init__(self, data):
      self.data = data
      self.prev = None
      self.next = None

# SOAL 1 DAN 2: MENAMBAH, MENAMPILKAN, DAN MENGHAPUS ANTRIAN
class DoubleLinkedList:
   def __init__(self):
      self.head = None

   def tambah_kendaraan(self, data):
      new_node = Node(data)

      # Jika linked list kosong
      if self.head == None:
         self.head = new_node
         return

      #Jika linked list tidak kosong
      current = self.head
      while current.next:
         current = current.next
      current.next = new_node
      new_node.prev = current

   def tampilkan_maju(self):
      # Jika linked list kosong
      if self.head == None:
         print('Tidak ada kendaraan.')
      
      # Jika antrian tidak kosong
      current = self.head
      while current:
         print(current.data)
         current = current.next

   def tampilkan_mundur(self):
      # Pergi dari head ke tail
      current = self.head
      while current and current.next:
         current = current.next

      # Menmpilkan data mundur
      while current:
         print(current.data)
         current = current.prev
      print('Tidak ada kendaraan.')

   def hapus_kendaraan(self, plat):
      current = self.head

      while current:
         if current.data == plat:
         # Jika node pertama
            if current.prev is None:
               self.head = current.next
               if self.head:
                  self.head.prev = None
               else:
                  # Menghubungkan node sebelumnya dengan node berikutnya
                  current.prev.next = current.next

                  if current.next:
                     # Menghubungkan node berikutnya dengan node sebelumnya
                     current.next.prev = current.prev
            return
         current = current.next


satu = DoubleLinkedList()
satu.tambah_kendaraan("B 1234 ABC")
satu.tambah_kendaraan("D 5678 XYZ")
satu.tambah_kendaraan("A 9999 TUV")
print('===== SOAL 1 =====')
print('[Maju]')
satu.tampilkan_maju()
print('\n[Mundur]')
satu.tampilkan_mundur()

print('\n===== SOAL 2 =====')
dua = DoubleLinkedList()
dua.tambah_kendaraan("B 1111 AA")
dua.tambah_kendaraan("D 2222 BB")
dua.tambah_kendaraan("A 3333 CC")
dua.tambah_kendaraan("B 4444 DD")
print("Sebelum:")
dua.tampilkan_maju()
dua.hapus_kendaraan("A 3333 CC")
print("\nSesudah:")
dua.tampilkan_maju()

# SOAL 3: CIRCULAR LINKED LIST
class Node:
   def __init__(self, data):
      self.data =  data
      self.next = None

class CircularLinkedList:
   def __init__(self):
      self.head = None

   def tambah_petugas(self, nama):
      new_node = Node(nama)

      if self.head == None:
         self.head = new_node
         new_node.next = self.head
         return
      
      current = self.head
      while current.next != self.head:
         current = current.next

      current.next = new_node
      new_node.next = self.head

   def giliran_berikutnya(self, n):
      current = self.head

      for x in range(n):
         print(f'Giliran {x+1}: {current.data}')
         current = current.next
      current = self.head

tiga = CircularLinkedList()
tiga.tambah_petugas("Andi")
tiga.tambah_petugas("Budi")
tiga.tambah_petugas("Citra")
tiga.tambah_petugas("Dewi")
print('\n===== SOAL 3 =====')
tiga.giliran_berikutnya(6)