def func(aaa, bbb):
	def fun(hand):
		if 'call' not in dir(hand):
			hand.call = {}
			print("####", aaa, "===")
		else:
			print("$$$$", bbb, "---")
		return hand
	return fun
