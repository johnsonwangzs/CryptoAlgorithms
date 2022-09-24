# -*- coding: utf-8 -*-
# @Time     : 2022/9/24 16:20
# @Author   : WZS
# @File     : Affine.py
# @Software : PyCharm
# @Function : Affine cipher.


from tools.math_calculate import extended_gcd


class AffineCipher:
    """
    Affine Cipher turns a string to another string, using parameters k and b.
    Encryption: for each plain character 'x', use 'y=k*x+b' to caculate the cipher character 'y'.
    """
    def __init__(self, k, b):
        """
        Initialize the parameters.
        :param k: A integer, represents a parameter.
        :param b: A integer, represents a parameter.
        """
        self.k = k
        self.b = b
        self.kInv = extended_gcd(self.k, 26)[1]

    def encrypt(self, m):
        """
        Affine Cipher - Encrypt
        :param m: A string, represents the plaintext.
        :return: The ciphertext.
        """
        m1 = list(m)
        for i in range(len(m)):
            if 'a' <= m[i] <= 'z':
                m1[i] = chr(((ord(m[i]) - 97) * self.k + self.b) % 26 + 97)
            elif 'A' <= m[i] <= 'Z':
                m1[i] = chr(((ord(m[i]) - 65) * self.k + self.b) % 26 + 65)
            elif '0' <= m[i] <= '9':
                m1[i] = chr(((ord(m[i]) - 48) * self.k + self.b) % 10 + 48)
            else:
                raise Exception('The string you input should only contains a~z,A~Z,0~9.')
        return ''.join(m1)  # Convert list to string

    def decrypt(self, c):
        """
        Affine Cipher - Decrypt
        :param c: A string, represents the ciphertext.
        :return: The plaintext.
        """
        c1 = list(c)
        for i in range(len(c)):
            if 'a' <= c[i] <= 'z':
                c1[i] = chr(((ord(c[i]) - 97 - self.b) * self.kInv) % 26 + 97)
            elif 'A' <= c[i] <= 'Z':
                c1[i] = chr(((ord(c[i]) - 65 - self.b) * self.kInv) % 26 + 65)
            elif '0' <= c[i] <= '9':
                c1[i] = chr(((ord(c[i]) - 48 - self.b) * self.kInv) % 10 + 48)
            else:
                raise Exception('The string you input should only contains a~z,A~Z,0~9.')
        return ''.join(c1)


# Test encryption and decryption
affineCipher = AffineCipher(7, 10)
print(affineCipher.encrypt("Crypt0graphy"))
print(affineCipher.decrypt("Yzwln0azklhw"))
