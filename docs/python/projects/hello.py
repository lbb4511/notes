#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
print("hello python")

max = 10
sum = 0
extra = 0

"""

"""
for num in range(1, max):
    if num % 2 and not num % 3:
        print(sum)
        sum += num
    else:
        extra += 1

print(sum)

x = 'runoob'
sys.stdout.write(x + '\n')

x = "a"
y = "b"

print(x)
print(x, end=" ")
print(x, end="")
print(y, end=" ")
print()
