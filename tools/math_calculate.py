# -*- coding: utf-8 -*-
# @Time     : 2022/9/24 16:22
# @Author   : WZS
# @File     : math_calculate.py
# @Software : PyCharm
# @Function : Some useful functions for caculating.


def extended_gcd(a, b):
    """
    This function is used to caculate Extended Euclid Algorithm.
    It results in the GCD(greatest common divisor) of 'a' and 'b'.
    It also shows 'x' and 'y' which satisfy the equation 'x*a+y*b=1'.
    Furthermore, 'x' may also be called as the inverse element of 'a mod b'.
    :param a: An integer. Represents the first number.
    :param b: An integer. Represents the second number.
    :return: gcd(a,b); x and y which satisfy the equation x*a+y*b=1.
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, xtmp, ytmp = extended_gcd(b, a % b)
        x = ytmp
        y = xtmp - int(a // b) * ytmp
        return gcd, x, y


def
