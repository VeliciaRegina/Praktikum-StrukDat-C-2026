class Node:
   def __init__(self, nama, keluhan):
      self.data = [nama, keluhan]
      self.next = None

class Queue:
   def __init__(self):
      self.front = None
      self.rear = None
      self.length = 0

   def enqueue(self, nama, keluhan):
      new_node = Node(nama, keluhan)
      if self.rear is None:
         self.front = self.rear = new_node
         self.length += 1
         return
      self.rear.next = new_node
      self.rear = new_node
      self.length += 1

   def dequeue(self):
      if self.isEmpty():
         return "Queue is empty"
      temp = self.front
      self.front = temp.next
      self.length -= 1
      if self.front is None:
         self.rear = None
      return temp.data

   def peek(self):
      if self.isEmpty():
         return "Antian masih kosong"
      else:
         return self.front.data

   def isEmpty(self):
      return self.length == 0
         
   def size(self):
      return self.length

   def printQueue(self):
      temp = self.front
      posisi = 1
      while temp:
         print(f'{posisi}. Nama: {temp.data[0]} | Keluhan: {temp.data[1]}')
         temp = temp.next
         posisi +=1
      
   def clearQueque(self):
      self.front = None
      self.rear = None
      self.length = 0

# Create a queue
myQueue = Queue()
print('==============================')
print('SISTEM ANTRIAN POLI UMUM')
print('RS Sehat Bersama')
print('==============================')
print(f'\nApakah antrian kosong?', myQueue.peek())
myQueue.enqueue('Budi', 'demam tinggi')
myQueue.enqueue('Ani', 'batuk pilek')
myQueue.enqueue('Citra', ' sakit kepala')

print("\nAntrian Saat Ini: ")
myQueue.printQueue()
print(f'Jumlah pasien menunggu: ', myQueue.size())

peekNama, peekKeluhan = myQueue.peek()
print(f"\nPasien berikutnya: {peekNama} - {peekKeluhan}")

dequeNama, dequeKeluhan = myQueue.dequeue()
print(f"Dokter memanggil: {dequeNama} - {dequeKeluhan}")

myQueue.enqueue('Dodi', ' sakit kepala')

print("\nAntrian Saat Ini:")
myQueue.printQueue()

dequeNama, dequeKeluhan = myQueue.dequeue()
print(f"\nDokter memanggil: {dequeNama} - {dequeKeluhan}")
print(f'Jumlah pasien menunggu: ', myQueue.size())


print (f'Sesi poliklinik selesai. Antrian dikosongkan.')

myQueue.clearQueque()
status_akhir = 'Ya, antrian kosong' if myQueue.isEmpty() else 'Tidak kosong'
print('Apakah antrian kosong? ', status_akhir)