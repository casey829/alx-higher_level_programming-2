#!/usr/bin/python3
    if number >= 0:
        l_digit = number % 10
    else:
        l_digit = number % -10
        l_digit *= -1
    print("{:d}".format(l_digit), end='')
    return (l_digit)
