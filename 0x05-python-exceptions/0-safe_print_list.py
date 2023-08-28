#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	"""function about print element of list
	arg : my_list and x number of element
	"""
	print_element = 0
	try:
		for i in range(x):
			if print_element >= x:
				break
			print("{}".format(my_list[i]), end = '')
			print_element += 1
	except IndexError:
		pass
	finally:
		print()
	return (print_element)
