"""
Implement a BST
"""

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None 

class Binary_Search_Tree:
	def __init__(self):
		self.root = None

	def insert(self, value):
		node = Node(value)
		if self.root == None:
			self.root = node
			return

		ptr = self.root
		while True:
			if value < ptr.value:
				if ptr.left == None:
					ptr.left = node
					return
				else:
					ptr = ptr.left
			elif value > ptr.value:
				if ptr.right == None:
					ptr.right = node
					return
				else:
					ptr = ptr.right
		"""
		while ptr:
			#print ("ptr=%s" % ptr.value)
			prev = ptr
			right = left = 0
			if value > ptr.value:
				ptr = ptr.right
				right = 1
			elif value < ptr.value:
				ptr = ptr.left
				left = 1

		if right:
			prev.right = node
			print ("prev=%s prev.right=%s" % (prev.value, prev.right.value))
		elif left:
			prev.left = node
			print ("prev=%s prev.left=%s" % (prev.value, prev.left.value))
		"""

	def lookup(self, value):
		ptr = self.root
		while ptr:
			#print ("ptr=%s value=%s" % (ptr.value, value))
			if value > ptr.value:
				ptr = ptr.right
			elif value < ptr.value:
				ptr = ptr.left
			elif value == ptr.value:
				return "found"

		return "Not found"	

	def remove(self, value):
		#TODO
		pass

	def traverse(self, node):
		print (node.value)
		if node.left:
			self.traverse(node.left)
		if node.right:
			self.traverse(node.right)


		
tree = Binary_Search_Tree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.traverse(tree.root)
print (tree.lookup(9))
print (tree.lookup(4))
print (tree.lookup(20))
print (tree.lookup(6))
print (tree.lookup(1))
print (tree.lookup(170))
print (tree.lookup(15))
print (tree.lookup(3))
tree.remove(6)
tree.traverse(tree.root)


			
				
			


