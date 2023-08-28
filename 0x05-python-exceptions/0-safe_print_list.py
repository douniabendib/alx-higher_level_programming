#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	"""function about print element of list
	arg : my_list and x number of element
	"""
	print_element = 0
	for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            print_element += 1
        except IndexError:
            break
    print("")
    return (print_element)
