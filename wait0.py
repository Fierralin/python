import threading

def input_fun(context):
	context['data'] = input('input: ')

context = {'data' : 'default'}
t = threading.Thread(target = input_fun, args=(context,))
t.start()
t.join(4)
if (context['data'] == 'default'):
	print('\ntime out')
print(context)
