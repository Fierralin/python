import threading

def edit__(val):
	val[0] = input('Type 1 to add flows: ')

val = [0]
thr = threading.Thread(target = edit__, args = (val,))
thr.start()
thr.join(3)

print val[0]
if (val[0] == 1):
	kaka = raw_input("flow talbe: ")
	print kaka
else:
	print "nothing"
