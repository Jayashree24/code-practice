class Stack:
	def __init__(self):
		self.list = []

	def push(self, value):
		self.list.append(value)

	def peek(self):
		if self.list:
			return self.list[-1]

	def pop(self):
		if self.list:
			return self.list.pop()
		
	def isEmpty(self):
		return len(self.list)

	def print_stack(self):
		for i in self.list:
			print (i)

s = Stack()
s.push('google.com')
s.push('youtube.com')
s.push('gmail.com')
s.push('netflix.com')

#s.print_stack()

print (s.isEmpty())

while s.isEmpty():
	print (s.pop())
