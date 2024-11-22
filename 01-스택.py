class Stack:
	def __init__(self):
		self.items = []
		
	def is_empty(self):
		return len(self.items) == 0
	
	def push(self, item):
		self.items.append(item)
	
	def pop(self):
		if (not self.is_empty()):
			return self.items.pop()
		else:
			return None
	
	def peek(self):
		if (not self.is_empty()):
			return self.items[-1]
		else:
			return None
	
	def size(self):
		return len(self.items)

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("스택 크기:", stack.size())
print("스택 최상단 요소:", stack.peek())
print("스택에서 꺼낸 요소:", stack.pop())
print("스택 크기:", stack.size())
print("스택이 비어 있는가:", stack.is_empty())