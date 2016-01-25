#class claa(object):
class claa:
	def __init__(self):
		self.aaa = 100
	def foo(self):
		print self.aaa

class clab(claa):
	def __init__(self):
		#super(clab, self).__init__()
		claa.__init__(self)
	def foo1(self):
		# print super(clab, self).aaa
		#super(clab, self).foo()
		claa.foo(self)
		print "dddd"
c = clab()
c.foo1()
