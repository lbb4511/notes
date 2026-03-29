
# -*- coding: UTF-8 -*-

# Filename : test.py
# author by : www.runoob.com

import cmath

num = float(input('请输入一个数字： '))
num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f' % (num, num_sqrt))


num = int(input("请输入一个数字: "))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))
