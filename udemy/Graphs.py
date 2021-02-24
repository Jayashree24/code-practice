"""
Implement Graphs
"""

class Graph:
	def __init__(self):
		self.numofnodes = 0
		self.adjacentlist = {}

	
	def addVertex(self, node):
		self.adjacentlist[node] = []
		self.numofnodes += 1
		#print ("nodes=%s adjacentlist=%s" % (self.numofnodes, self.adjacentlist))

	def addEdge(self, node1, node2):
		self.adjacentlist[node1].append(node2)
		self.adjacentlist[node2].append(node1)
		#print (self.adjacentlist)

	def showConnections(self):
		for i, j in self.adjacentlist.items():
			x = '%s ----> %s' % (i, ' '.join(j))
			print (x)


myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1') 
myGraph.addEdge('3', '4') 
myGraph.addEdge('4', '2') 
myGraph.addEdge('4', '5') 
myGraph.addEdge('1', '2') 
myGraph.addEdge('1', '0') 
myGraph.addEdge('0', '2') 
myGraph.addEdge('6', '5')
myGraph.showConnections()



