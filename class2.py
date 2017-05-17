class ccc:
	def __init__(self, a = "abc"):
		self.abc = a
	def __call__(self):
		#self.abc = "dddd"
		print("%s __call__" % self.abc)

@ccc
def fun():
	print(" fun===")

fun()
