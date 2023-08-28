#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    try:
        for item in my_list:
            try:
                formatted_item = "{:d}".format(item)
                print(formatted_item, end=' ')
                printed_integers += 1
                if printed_integers >= x:
                    break
            except ValueError:
                pass
    except IndexError:
        pass  

    print()
    return printed_integers
