def f1(arg):
    print "f1"
    rl = arg("^^")
    print rl
    return rl + "f1"

@f1
def f2(arg = "__"):
    print "f2"
    return arg + "f2r"

#print "start"
#print f1
