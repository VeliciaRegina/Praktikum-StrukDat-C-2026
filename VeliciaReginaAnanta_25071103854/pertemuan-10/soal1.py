class StackList:
   def __init__(self):
      self.stack = []

   def is_empty(self):
      return len(self.stack) == 0

   def push(self, url):
      self.stack.append(url)

   def pop(self):
      if self.is_empty():
         return "Stack is empty"
      return self.stack.pop()

   def peek(self):
      if self.is_empty():
         return "Stack is empty"
      return self.stack[-1]

   def size(self):
      return len(self.stack)

# Create a stack
myStack = StackList()
myStack.push('https:/cia')
myStack.push('https:/dina')
myStack.push('https:/nur')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.is_empty())
print("Size: ", myStack.size())