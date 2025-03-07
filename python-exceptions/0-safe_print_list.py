#!/usr/bin/python3
def safe_print_list(my_list=[], y=0):
    num = 0
    for i in range(y):
        try:
            print(my_list[i], end="")
            num += 1
        except IndexError:
            break
    print()
    return num
