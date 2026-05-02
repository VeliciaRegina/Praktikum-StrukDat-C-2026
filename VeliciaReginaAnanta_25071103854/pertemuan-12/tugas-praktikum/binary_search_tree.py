class Node:
   def __init__(self, id_buku, judul):
      self.id_buku = id_buku
      self.judul = judul
      self.left = None
      self.right = None

class BinarySearchtree:
   def __init__(self):
      self.root = None

   def insert(self, id_buku, judul):
      def _insert(node, id_buku, judul):
         if node == None:
            return Node(id_buku, judul)
         
         if id_buku < node.id_buku:
            node.left = _insert(node.left, id_buku, judul)
         else:
            node.right = _insert(node.right, id_buku, judul)
         return node

      self.root = _insert(self.root, id_buku, judul)
      print(f'[INSERT] Berhasil memasukkan ID {id_buku} - {judul}')

   def search(self, id_buku):
      def _search(node, id_buku):
         if node == None:
            return None
         if node.id_buku == id_buku:
            return node
         elif id_buku < node.id_buku:
            return _search(node.left, id_buku)
         else:
            return _search(node.right, id_buku)
      
      hasil = _search(self.root, id_buku)
      if hasil:
         print(f'[SEARCH] Mencari ID {id_buku}... Ditemukan! Judul: {hasil.judul}')
      else:
         print(f'[SEARCH] Mencari ID {id_buku}... Data tidak ditemukan.')

   def traversal_inorder(self):
      print(f'[INFO] Koleksi Buku (In-Order Traversal):')
      def _inorder(node):
         nonlocal nomor
         if node == None:
            return 'Katalog kosong'

         _inorder(node.left)
         print(f'{nomor}. {node.id_buku} - {node.judul}')
         nomor += 1
         _inorder(node.right)
         
      nomor = 1
      _inorder(self.root)

   def get_min(self):
      node = self.root
      while node.left:
         node = node.left
      return node

   def get_max(self):
      node = self.root
      while node.right:
         node = node.right
      return node

   def height(self):
      def _height(node):
         if node == None:
            return -1
         return 1 + max(_height(node.left), _height(node.right))
      return _height(self.root)

#----------------------------------------------------------------------------
bst = BinarySearchtree()
print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print('=========================================')

bst.insert(50, 'Dasar Pemrograman')
bst.insert(30, 'Struktur Data')
bst.insert(70, 'Kecerdasan Buatan')
bst.insert(20, 'Matematka Diskrit')
bst.insert(40, 'Basis Data')
bst.insert(60, 'Jaringan Komputer')
bst.insert(80, 'Sistem Operasi')
print()

bst.traversal_inorder()
print()

bst.search(60)
bst.search(10)
bst.search(40)
bst.search(100)
print()

print(f'[STATISTIK] ID Terkecil: ', bst.get_min().id_buku)
print(f'[STATISTIK] ID Terbesar: ', bst.get_max().id_buku)
print()

print(f'[INFO] Tinggi (Height) Tree: {bst.height()}')

print("=========================================")
print("Simulasi Selesai!")
