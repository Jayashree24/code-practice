class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Stack:
	def __init__(self):
		self.top = None
		self.bottom = None
		self.length = 0

	def push(self, value):
		node = Node(value)
		if self.length == 0:
			self.top = self.bottom = node
		else:
			node.next = self.top
			self.top = node
		self.length += 1

	def peek(self):
		if self.length:
			return self.top.value

	def pop(self):
		if self.length:
			ptr = self.top
			self.top = self.top.next
			self.length -= 1
			return ptr.value
		else:
			self.bottom = None
		
	def isEmpty(self):
		if self.length == 0:
			self.bottom = None
		return self.length

	def print_stack(self):
		ptr = self.top
		while (ptr):
			print (ptr.value)
			ptr = ptr.next
		
		
s = Stack()
s.push('google.com')
s.push('youtube.com')
s.push('gmail.com')
s.push('netflix.com')

#s.print_stack()

print (s.length)
while s.isEmpty():
	print (s.pop())

