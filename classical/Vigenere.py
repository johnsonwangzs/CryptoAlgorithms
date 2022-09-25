# -*- coding: utf-8 -*-
# @Time     : 2022/9/24 18:03
# @Author   : WZS
# @File     : Vigenere.py
# @Software : PyCharm
# @Function : The Vigenere Cipher.


class VigenereCipher:
    """
    Vigenere Cipher simply adds each character in plaintext with each character in key.
    """
    def __init__(self, key):
        self.key = key

    def encrypt(self, m):
        """
        Vigenere Cipher - Encrypt
        :param m: A string, represnts the plaintext.
        :return: The ciphertext.
        """
        p = 0  # 指示key中字符位置的指针
        m1 = list(m)
        for i in range(len(m)):
            if p == len(self.key):
                p = 0
            m1[i] = chr(((ord(m[i]) - 97) + (ord(self.key[p]) - 97)) % 26 + 97)
            p += 1
        return ''.join(m1)

    def decrypt(self, c):
        """
        Vigenere Cipher - Decrypt
        :param c: A string, represnts the ciphertext.
        :return: The plaintext.
        """
        p = 0
        c1 = list(c)
        for i in range(len(c)):
            if p == len(self.key):
                p = 0
            c1[i] = chr(((ord(c[i]) - 97) - (ord(self.key[p]) - 97)) % 26 + 97)
            p += 1
        return ''.join(c1)


# Test encryption and decryption
vigenereCipher = VigenereCipher("interesting")
print(vigenereCipher.decrypt(vigenereCipher.encrypt("zhonghuaminzuweidafuxing")))