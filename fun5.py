def foo(tmp):
	#print "foo"
	a = tmp.__name__ + " return"
	tmpa = tmp(a)
	return tmpa
@foo
def fpp(a = ""):
	print(a + " _fpp")
	return a + " _fpp"


#fpp()
fpp()
#print fpp("aaa")

