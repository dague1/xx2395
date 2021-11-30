#!/usr/bin/env python3
from insecure_hash import hash_string
from Crypto.Cipher import AES
import string
import random


def find_collision(message):
    hash = hash_string(message)
    key = 'aaaaaaaaaaaaaaaa'.encode()
    c = AES.new(key)
    print(c)
    res = c.encrypt(hash)
    res= res + key
    #print res test tests
    print(res)
    return res

if __name__ == '__main__':
    message = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb".encode()
    print("Hash of %s is %s" % (message, hash_string(message)))
    collision = find_collision(message)
    print("Hash of %s is %s" % (collision, hash_string(collision)))
