class ABC:
	def __init__(self):
		self.a = 0
		self.b = 1
		self.c = 2
	def printf(self):
		print("a:", self.a, " b:", self.b, " c:", self.c)

aaa = ABC()
bbb = aaa
bbb.a = 3
aaa.printf()

ccc = ABC()
ccc.a = 4
ccc = aaa
ccc.printf()
ccc.c = 6
aaa.printf()
