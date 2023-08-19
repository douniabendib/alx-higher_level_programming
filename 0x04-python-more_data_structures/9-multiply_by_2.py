#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    key_list = list(new_dic.keys())

    for i in key_list:
        new_dic[i] = 2 * new_dic[i]

    return (new_dic)
