#!/usr/bin/python3
letter = input("type a word: ").lower().strip()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
for x in letter:
    if x not in vowels:
        print(x, end=', ')
    else:
        continue
