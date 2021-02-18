class Node:
	def __init__(self, value):
		self.value = value
		self.next = None 

class Queue:
	def __init__(self):
		self.first = None 
		self.last = None 
		self.length = 0

	def enqueue(self, value):
		node = Node(value)
		if self.length == 0:
			self.first = self.last = node
		else:
			self.last.next = node
			self.last = node
		self.length += 1

	def dequeue(self):
		if self.length:
			x = self.first
			self.first = self.first.next
			self.length -= 1
			return x.value
		else:
			self.last = None

	def peek(self):
		if self.length:
			return self.first.value

	def print_queue(self):
		ptr = self.first
		while ptr:
			n = None
			if ptr.next:
				n = ptr.next.value
			print ('***')
			print (ptr.value, n)
			ptr = ptr.next

	
			

q = Queue()
q.enqueue('Joy')
q.enqueue('Pink')
q.enqueue('Tree')
q.enqueue('Hiyta')

print (q.dequeue())
print (q.peek())
print (q.dequeue())


#q.print_queue()

