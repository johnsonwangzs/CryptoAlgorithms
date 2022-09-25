# -*- coding: utf-8 -*-
# @Time     : 2022/9/24 22:23
# @Author   : WZS
# @File     : Vernam.py.py
# @Software : PyCharm
# @Function : Vernam Cipher.


class VernamCipher:
    """
    Vernam Cipher - One time one key.
    SimpleXOR caculation.
    """
    def __init__(self, key):
        """
        Initialize Vernam Cipher.
        :param key: An string, represents the key.
        """
        self.key = key

    def _check_len(self, s):
        if len(self.key) != len(s):
            raise Exception('\'One time one key\' requires the length of key and the length of text to be equal.')

    def encrypt(self, m):
        """
        Vernam Encrypt.
        :param m: A string. The plaintext.
        :return: A string. The ciphertext.
        """
        self._check_len(m)
        c = []
        for i in range(len(m)):
            c.append(chr(ord(m[i]) ^ ord(self.key[i])))
        return ''.join(c)

    def decrypt(self, c):
        """
        Vernam Decrypt.
        :param c: A string. The ciphertext.
        :return: A string. The plaintext.
        """
        self._check_len(c)
        m = []
        for i in range(len(c)):
            if c[i] == '\n':
                m.append(chr(ord('\r') ^ ord(self.key[i])))
            else:
                m.append(chr(ord(c[i]) ^ ord(self.key[i])))
        return ''.join(m)


# Test encryption and decryption
vernamCipher = VernamCipher('helloworld!')
print(vernamCipher.decrypt(vernamCipher.encrypt('12345678910')))
