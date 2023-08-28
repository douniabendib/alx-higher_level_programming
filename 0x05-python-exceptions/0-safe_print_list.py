#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	print_element = 0
	try:
		for i in my_list:
			if print_element >= x:
				break
			print(i, end = '')
			print_element += 1
	except IndexError:
		pass
	finally:
		print()
	return print_element
