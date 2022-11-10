#!/usr/bin/python3
# checks if a number is weird or not weird

def weird(m):
    if m % 2 != 0:
        if m > 3 and m < 6:
            return print('Not Weird')
        if m > 6 and m < 21:
            return print('Weird')
        if m > 20:
            return print('Not Weird')
    else:
        return print('Weird')


is_weird = weird(89)
print(is_weird)
