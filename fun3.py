def foo(tmp):
	#print "foo"
	a = tmp.__name__ + " return"
	tmp(a)
	return tmp
@foo
def fpp(a = ""):
	print a + " _fpp"
	return a + " _fpp"


#fpp()
fpp("aaa")
#print fpp("aaa")
