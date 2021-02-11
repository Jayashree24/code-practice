class Node:
	def __init__(self, value):
		self.value = value
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
			#print ("tail=%s value=%s next=%s" % (self.tail, self.tail.value, self.tail.next))
			self.tail = node
			#self.tail.next = node
			#print ("tail=%s value=%s next=%s" % (self.tail, self.tail.value, self.tail.next))
		self.length += 1

	def prepend(self, value):
		# Add to the start of the linked list
		node = Node(value)
		node.next = self.head
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
		node.next = temp
		self.length += 1

	def prin(self, s=""):
		print (s)
		ptr = self.head
		l = []
		while ptr:
			#print (ptr.value)
			l.append(ptr.value)
			ptr = ptr.next
		print ('%s length=%s' % (l, self.length))

	def remove(self, index):
		if index == 0:
			temp = self.head
			self.head = self.head.next
			del temp
			self.length -= 1
			return
		elif index <= self.length:

			ptr = self.head
			for i in range(index-1):
				ptr = ptr.next

			#print (ptr.value, ptr.next.value, ptr.next.next)
			ptr.next = ptr.next.next

			if index == (self.length - 1):
				#print (self.tail.value), self.tail.next
				self.tail = ptr
				#print (self.tail.value, self.tail.next)
			del ptr
			self.length -= 1
			return
		elif index > self.length:
			return

	def reverse(self):
    		self.tail = self.head 

		"""
		first = self.head
		second = first.next
		self.head.next = None

		while second:
			temp = second.next
			#print (first.value, second.value, temp.value)
			second.next = first
			first = second
			second = temp
			self.head = first
			self.prin()

		"""

		prev = None
		ptr = self.head
		while ptr:
			#s = t = None
			#if prev:
			#	s = prev.value
			#if ptr.next:
			#	t = ptr.next.value
			#print (s, ptr.value, t)

			next = ptr.next
			ptr.next = prev
			prev = ptr
			ptr = next
			self.head = prev
			self.prin()
	
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
l.reverse()
l.prin("After reverse")
