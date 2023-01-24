#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        index = 0
        while my_list:
            if index == x:
                break
            print("{:d}".format(my_list[index]), end="")
            index += 1
        print("")
        return index
    except IndexError:
        print("")
        return index
