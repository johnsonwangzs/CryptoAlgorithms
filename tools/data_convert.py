# -*- coding: utf-8 -*-
# @Time     : 2022/9/24 15:53
# @Author   : WZS
# @File     : data_convert.py
# @Software : PyCharm
# @Function : Convert data between different types.


def _int2str_dec(a):
    """
    Convert a integer to a string presented in decimal format.
    :param a: An integer, represents a number.
    :return: A string.
    """
    return str(a)


def _int2str_hex(a):
    """
    Convert an interger to a string presented in hexadecimal format.
    :param a: An interger, represents a number.
    :return: A string.
    """
    hexDict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    tmp = a
    s = ''
    while True:
        r = tmp - tmp // 16 * 16
        if tmp == 0:
            break
        if r >= 10:
            s = hexDict[r] + s
        else:
            s = str(r) + s
        tmp = tmp // 16
    return s


def _int2str_bin(a):
    """
    Convert an integer to a string presented in binary format.
    :param a: An integer, represents a number.
    :return: A string.
    """
    tmp = a
    s = ''
    while True:
        r = tmp - tmp // 2 * 2
        if tmp == 0:
            break
        s = str(r) + s
        tmp = tmp // 2
    return s


def int2str(a, base=10):
    """
    Convert an integer to a string.
    The result can be presented in forms of decimal/hexadecimal/binary.
    :param a: An integer, represents a number.
    :param base: An integer, represents the target base. Allow 10(default), 16 or 2.
    :return: A string.
    """
    if base != 10 and base != 16 and base != 2:
        raise Exception("The base must be 10, 16 or 2.")
    if base == 10:
        s = _int2str_dec(a)
    elif base == 16:
        s = _int2str_hex(a)
    else:
        s = _int2str_bin(a)
    return s


def str2int(s, base=10):
    """
    Convert a string to an integer.
    :param s: A string, represents a number.
    :param base: An integer, represents the original base.
    :return: An integer.
    """
    return int(s, base=base)