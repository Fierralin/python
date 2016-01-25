#!/bin/lib/python

class Man:
	def __init__(self, name = "TOM", age = "20", weight = "55"):
		self.name = name
		self.age = age
		self.__weight = weight
	def show(self):
		print self.name, "'s age: ", self.age
		self.hair = 12
	def show2(self):
		print self.__weight

tom = Man()
ace = Man("Ace", "25", "55")

import temp
from temp import KKK

ace.show()
ace.show2()
bbb=KKK()
tom.show()


