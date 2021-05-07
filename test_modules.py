import unittest
import os
import string
import subprocess
from socket import *
from threading import *
import random
from termcolor import colored
import scapy.all as scapy
from modules import CaeserCipher
from modules import PassGenerator

class TestCaeserCipher(unittest.TestCase):
    def test_encryption(self):
        self.assertAlmostEqual(CaeserCipher("hello",0).encrypt(),"hello")
        self.assertAlmostEqual(CaeserCipher("hello",1).encrypt(),"ifmmp")
        self.assertAlmostEqual(CaeserCipher("hello",-1).encrypt(),"gdkkn")
        self.assertRaises(ValueError,CaeserCipher("1234",2).encrypt)  # --> test failed
    
    def test_decryption(self):
        self.assertAlmostEqual(CaeserCipher("hello",0).decrypt(),"hello")
        self.assertAlmostEqual(CaeserCipher("ifmmp",1).decrypt(),"hello")
        self.assertAlmostEqual(CaeserCipher("gdkkn",-1).decrypt(),"hello")
        self.assertRaises(ValueError,CaeserCipher("1234",2).decrypt)  # --> test failed

