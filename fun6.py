def foo6(tmp, arg = "", arh = ""):
	print "foo6 only" + arg + arh
	return True

@foo6
def foo(arg = "__"):
	print "foo only" + arg

print foo
