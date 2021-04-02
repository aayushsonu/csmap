#!/usr/bin/python3

'''
C-Caeser Cipher
S-Strong password generator
M-Mac Spoofer
A-Arp scanner
P-port scanner
This will be a command line project with some web interface that may be run on localhost.
I am going to use sys module , os module and some extra related modules.

'''

import sys
import os


class CaeserCipher:
    def __init__(self, text,s):
        self.text=text
        self.s=s

    def encrypt(self): 
        result = "" 
    
        # traverse text 
        for i in range(len(self.text)): 
            char = self.text[i] 
    
            # Encrypt uppercase characters 
            if (char.isupper()): 
                result += chr((ord(char) + self.s-65) % 26 + 65) 
    
            # Encrypt lowercase characters 
            else: 
                result += chr((ord(char) + self.s - 97) % 26 + 97) 
    
        return result 


class PassGenerator:
    def __init__(self):
        print("hey here i will create a Random Password Generator program")


class MacSpoofer:
    def __init__(self):
        print("hey here i will create a MacSpoofer program")


class ArpSpoofer:
    def __init__(self):
        print("hey here i will create a ArpSpoofer program")


class PortScanner:
    def __init__(self):
        print("hey here i will create a PortScanner program")


if __name__ == "__main__":

    try:
        if len(sys.argv) == 1:
            print('''Tools: 
1.Caeser Cipher  
2.Strong password generator 
3.Mac Spoofer 
4.Arp scanner 
5.port scanner 
        ''')

        elif sys.argv[1] == 'help':
            print('''Tools: 
1.Caeser Cipher  
2.Strong password generator 
3.Mac Spoofer 
4.Arp scanner 
5.port scanner
        ''')

        elif len(sys.argv) > 1:
            text = sys.argv[1]
            s = int(sys.argv[2])
            c = CaeserCipher(text, s)
            print("Text  : " + text)
            print("Cipher: " + c.encrypt())

            # PassGenerator()
            # MacSpoofer()
            # ArpSpoofer()
            # PortScanner()
            # print(sys.argv[1])

    except:
        print("I will help you , dont worry!!")
