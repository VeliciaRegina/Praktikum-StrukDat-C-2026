class Node:
   def __init__(self, url):
      self.url = url
      self.next = None

class StackLinkedList:
   def __init__(self):
      self.top = None
      self.size = 0

   def push(self, value):
      new_node = Node(value)
      if self.top:
         new_node.next = self.top
      self.top= new_node
      self.size += 1

   def pop(self):
      if self.isEmpty():
         return "Stack is empty"
      popped_node = self.top
      self.top = self.top.next
      self.size -= 1
      return popped_node.url

   def peek(self):
      if self.isEmpty():
         return "Stack is empty"
      return self.top.url

   def isEmpty(self):
      return self.size == 0

   def stackSize(self):
      return self.size

   def traverseAndPrint(self):
      currentNode = self.top
      while currentNode:
         print(currentNode.url, end=" -> ")
         currentNode = currentNode.next
      print()

myStack = StackLinkedList()
myStack.push('https:/cia')
myStack.push('https:/dina')
myStack.push('https:/nur')

print("LinkedList: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.traverseAndPrint()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())