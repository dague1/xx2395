from crypto import *

class SecCrypto():
    def load_table(self, cache):
        for i in range(len(T)):
            cache.write_address(T_address+i, T[i])
    
    def feistel_encrypt(self, cache, msg, key):
        int1 = ord(msg[0])
        int2 = ord(msg[1])
        a = cache.read_address(int2)
        a = int1 ^ ord(key[0]) ^a[0]
        b = cache.read_address(a)
        cache.__init__() #1
        return chr(int2)+chr(int2 ^ ord(key[1]) ^b[0])

