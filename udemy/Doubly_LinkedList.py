class Node:
	def __init__(self, value):
		self.value = value
		self.prev = None
		self.next = None 

class LinkedList:
	def __init__(self):
		self.head = None 
		self.tail = None 
		self.length = 0

	def append(self, value):
		# Add to the end of the linked list
		node = Node(value)
		#print ("Node %s=%s" % (node.value, node.next))
		#if self.head:
		#	print ("head: value=%s next=%s" % (self.head.value, self.head.next))
		#if self.tail:
		#	print ("tail: value=%s next=%s" % (self.tail.value, self.tail.next))
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			#print ("tail=%s value=%s next=%s" % (self.tail, self.tail.value, self.tail.next))
			self.tail.next = node
			node.prev = self.tail
			#print ("tail=%s value=%s next=%s" % (self.tail, self.tail.value, self.tail.next))
			self.tail = node
			#print ("tail=%s value=%s next=%s" % (self.tail, self.tail.value, self.tail.next))
		self.length += 1

	def prepend(self, value):
		# Add to the start of the linked list
		node = Node(value)
		node.next = self.head
		self.head.prev = node
		self.head = node
		self.length += 1

	def insert(self, index, value):

		if index == 0:
			self.prepend(value)
			return
		elif index == self.length:
			self.append(value)
			return
		elif index > self.length:
			return

		ptr = self.head
		node = Node(value)

		for i in range(index-1):
			ptr = ptr.next

		#print (ptr.value, ptr.next.value)
		temp = ptr.next
		ptr.next = node
		node.prev = ptr
		node.next = temp
		temp.prev = node
		self.length += 1

	def prin(self, s=""):
		print (s)
		ptr = self.head
		l = []
		s = []
		while ptr:
			if ptr.prev is None:
				p = None
			else:
				p = ptr.prev.value
			if ptr.next is None:
				n = None
			else:
				n = ptr.next.value
			s.append([p, n])
			l.append(ptr.value)
			ptr = ptr.next
		print ('%s length=%s' % (l, self.length))
		#print (s)

	def remove(self, index):
		if index == 0:
			temp = self.head
			self.head = self.head.next
			del temp
			self.length -= 1
			return
		elif index == (self.length - 1):
			#print (self.tail.value, self.tail.next, self.tail.prev.value)
			self.tail = self.tail.prev
			self.tail.next = None
			#print (self.tail.value, self.tail.next, self.tail.prev.value)
		elif index <= self.length:

			ptr = self.head
			for i in range(index-1):
				ptr = ptr.next

			#print (ptr.value, ptr.next.value, ptr.next.next)
			ptr.next = ptr.next.next
			ptr.next.prev = ptr

			del ptr
			self.length -= 1
			return
		elif index > self.length:
			return
	
l = LinkedList()
l.append(5)
l.append(10)
l.append(15)
l.append(16)
l.append(18)
l.prin("After append")
l.prepend(1)
l.prin("After prepend 1")
l.insert(2, 24)
l.prin("After insert 24 at postion 2")
l.insert(5,44)
l.prin("After insert 44 at postion 5")
l.remove(7)
l.prin("After remove position 7")
l.prepend(2)
l.prin("After prepend 2")
l.append(4)
l.prin("After append 4")
l.insert(4, 78)
l.prin("After insert 78 at position 4")
l.remove(2)
l.prin("After remove position 2")
l.append(14)
l.prin("After append 14")
l.insert(7, 66)
l.prin("After insert 66 at position 7")
