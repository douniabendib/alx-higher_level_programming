#!/usr/bin/python3
def subtract(list_num):
    sub = 0
    max_list = max(list_num)
    for n in list_num:
        if max_list > n:
            sub = sub + n
            return (max_list - sub)
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keys_list = list(rom_num.keys())
    num = 0
    last_rom = 0
    list_num = [0]
    for ch in roman_string:
        for ro_num in keys_list:
            if ro_num == ch:
                if rom_n.get(ch) <= last_rom:
                    num = num + subtract(list_num)
                    list_num = [rom_num.get(ch)]
                else:
                    list_num.append(rom_num.get(ch))
                last_rom = rom_num.get(ch)
                num = num + subtract(list_num)
                return (num)


                                                                                                                                                                                                             
