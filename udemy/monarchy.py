"""
Desgin monarchy system
"""
class Person:
	def __init__(self, name):
		self.name = name
		self.alive = 1
		self.children = []

class Monarchy:
	def __init__(self, king):
		self.king = Person(king)
		self._persons = {self.king.name : self.king}

	def birth(self, child, parent):
		par = self._persons[parent]
		chd = Person(child)
		par.children.append(chd)
		self._persons[chd.name] = chd
		#print (self._persons.keys())

	def _dfs(self, node, order):
		while node:
			#print (node.name)
			if node.alive:
			    order.append(node.name)
			for i in node.children:
				self._dfs(i, order)
			else:
				return
	def getOrderOfSuccession(self):
		order = []
		self._dfs(self.king, order=order)
		print (order)

	def death(self, name):
		per = self._persons[name]
		per.alive = 0

mon = Monarchy('Jake')
mon.birth('Catherine', 'Jake')
mon.birth('Tom', 'Jake')
mon.birth('Celine', 'Jake')
mon.birth('Peter', 'Celine')
mon.birth('Jane', 'Catherine')
mon.birth('Farah', 'Jane')
mon.birth('Mark', 'Catherine')
mon.getOrderOfSuccession()
mon.death('Jake')
mon.death('Jane')
mon.getOrderOfSuccession()





