#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_integer = 0
    try:
        for item in my_list:
            try:
                formatt_item = "{:d}".format(item)
                print(formatt_item, end=' ')
                print_integer += 1
                if print_integer >= x:
                    break
            except ValueError:
                pass
    except IndexError:
        pass 

    print() 
    return print_integer
