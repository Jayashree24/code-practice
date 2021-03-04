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

	def breadth_first_search(self):
		current_node = self.root
		bfs_list = []
		bfs_queue = []
		bfs_queue.append(current_node)
		while bfs_queue:
			current_node = bfs_queue[0]
			#print (current_node.value)
			del bfs_queue[0]
			bfs_list.append(current_node.value)
			if current_node.left:
				bfs_queue.append(current_node.left)
			if current_node.right:
				bfs_queue.append(current_node.right)
		return bfs_list

	def breadth_first_search_recursive(self, bfs_queue, bfs_list):
		if not bfs_queue:
			return bfs_list
		#print (bfs_queue)
		current_node = bfs_queue[0]
		del bfs_queue[0]
		bfs_list.append(current_node.value)
		if current_node.left:
			bfs_queue.append(current_node.left)
		if current_node.right:
			bfs_queue.append(current_node.right)
		return self.breadth_first_search_recursive(bfs_queue, bfs_list)

	def dfs_in_order(self, node, bfs_list):
		l = r = None
		if node.left:
			l = node.left.value
		if node.right:
			r = node.right.value
		print ("left=%s val=%s right=%s" % (l, node.value, r))
		if node.left:
			self.dfs_in_order(node.left, bfs_list)
		bfs_list.append(node.value)
		print (bfs_list)
		if node.right:
			self.dfs_in_order(node.right, bfs_list)

		return bfs_list

	def dfs_pre_order(self, node, bfs_list):
                l = r = None
                if node.left:
                        l = node.left.value
                if node.right:
                        r = node.right.value
                print ("left=%s val=%s right=%s" % (l, node.value, r)) 
                bfs_list.append(node.value)
                print (bfs_list)
                if node.left:
                        self.dfs_pre_order(node.left, bfs_list)
                if node.right:
                        self.dfs_pre_order(node.right, bfs_list)

                return bfs_list
	def dfs_post_order(self, node, bfs_list):
		l = r = None
		if node.left:
                        l = node.left.value
		if node.right:
                        r = node.right.value
		print ("left=%s val=%s right=%s" % (l, node.value, r))
		if node.left:
                        self.dfs_post_order(node.left, bfs_list)
		if node.right:
                        self.dfs_post_order(node.right, bfs_list)
		bfs_list.append(node.value)
		print (bfs_list)

		return bfs_list

tree = Binary_Search_Tree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.traverse(tree.root)
print ('**********')
#print (tree.breadth_first_search())
#print (tree.breadth_first_search_recursive([tree.root], []))
#print (tree.dfs_in_order(tree.root, []))
#print (tree.dfs_pre_order(tree.root, []))
print (tree.dfs_post_order(tree.root, []))
print ('**********')
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


			
				
			


