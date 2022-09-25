# -*- coding: utf-8 -*-
# @Time     : 2022/9/25 9:40
# @Author   : WZS
# @File     : MonoSub.py
# @Software : PyCharm
# @Function : MonoSub Cipher.


class MonoSubCipher:
    def __init__(self, f):
        """
        Init sub list.
        :param f: sub list
        """
        self.f = f

    def encrypt(self, m):
        """
        MonoSubCipher - Encryption
        :param m: plaintext
        :return: ciphertext
        """
        m1 = list(m)
        for i in range(len(m)):
            if 'a' <= m[i] <= 'z':
                m1[i] = self.f[ord(m[i]) - 97]
            else:
                raise Exception('The input should only contains characters between \'a\' and \'z\'!')
        return ''.join(m1)

    def decrypt(self, c):
        """
        MonoSubCipher - Decryption
        :param c: ciphertext
        :return: plaintext
        """
        c1 = list(c)
        for i in range(len(c)):
            if 'a' <= c[i] <= 'z':
                p = self.f.find(c[i])  # p是密文字母在替换表中对应的下标
                c1[i] = chr(p + 97)
            else:
                raise Exception('The input should only contains characters between \'a\' and \'z\'!')
        return ''.join(c1)


# Test encryption and decryption
monoSubCipher = MonoSubCipher("qazwsxedcrfvtgbyhnujmiklop")
print(monoSubCipher.decrypt(monoSubCipher.encrypt("helloworld")))
