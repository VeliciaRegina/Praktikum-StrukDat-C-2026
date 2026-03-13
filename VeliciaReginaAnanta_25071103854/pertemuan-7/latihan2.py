
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None

def traverseAndPrint(head):
   currentNode = head
   while currentNode:
      print(currentNode.data, end=" -> ")
      currentNode = currentNode.next
   print("null")

def tambahKendaraan(head, newNode, position):
   currentNode = head
   for _ in range(position - 2):
      if currentNode is None:
         break
      currentNode = currentNode.next

   newNode.next = currentNode.next
   currentNode.next = newNode
   return head

def hapusKendaraan(head, nodeToDelete):
   if head == nodeToDelete:
      return head.next

   currentNode = head
   while currentNode.next and currentNode.next != nodeToDelete:
      currentNode = currentNode.next

   if currentNode.next is None:
      return head

   currentNode.next = currentNode.next.next

   return head


node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 111 TUV")
node4 = Node("B 2022 EFG")

node1.next = node2
node2.next = node3
node3.next = node4

newNode = Node("F 789 FGH")
node1 = tambahKendaraan(node1, newNode, 5)

print("\nSetelah insert:")
traverseAndPrint(node1)

node1 = hapusKendaraan(node1, node3)
print("\nSetelah delete:")
traverseAndPrint(node1)