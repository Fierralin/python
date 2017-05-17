def foo(tmp):
	#print "foo"
	a = "tmp return"
	tmp(a)
	return tmp

@foo
def fpp(a = ""):
	print(a + " _fpp")
	return a + " _fpp"


#fpp()
fpp("aaa")
#print fpp("aaa")
