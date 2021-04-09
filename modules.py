import os
import string
import subprocess
from socket import *
from threading import *
import random
from termcolor import colored
import scapy.all as scapy


class CaeserCipher:
    def __init__(self, text, s):
        self.text = text
        self.s = int(s)
    def encrypt(self):
        result = ""

        # traverse text
        for i in range(len(self.text)):
            char = self.text[i]

# ord can change alphabet to ascii
# chr can cahne ascii to alphabet

            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + self.s-65) % 26 + 65)

            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + self.s - 97) % 26 + 97)

        return result

    # I have to create a decrypt algo and there should be a concept of key.
    def decrypt(self):
        result = ""
        for i in range(len(self.text)):
            char = self.text[i]
            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) - 65) % 26 - self.s + 65)

            # Encrypt lowercase characters
            else:
                result += chr((ord(char) - 97) % 26 - self.s + 97)

        return result


class PassGenerator:
    def __init__(self, l):
        self.s1 = list(string.ascii_lowercase)
        self.s2 = list(string.ascii_uppercase)
        self.s3 = list(string.digits)
        self.s4 = list(string.punctuation)
        self.s = []
        self.s.extend(self.s1)
        self.s.extend(self.s2)
        self.s.extend(self.s3)
        self.s.extend(self.s4)
        self.passlen = l

        if self.passlen < 8:
            print(colored('''\tYou entered a length which is too small.
        Its easy to crack by any Cracker..
        So, I will create a 8 letters password for you
        I hope you dont mind it''', 'yellow'))
            print(colored("".join(random.sample(self.s, 8)),
                          'green', attrs=['bold', 'blink']))
        elif self.passlen > 94:
            print(
                colored(f"Where to use {self.passlen} letters password LOL", 'yellow'))
            print(colored(
                f"If you really want to create a password of {self.passlen} letters then Enter", 'blue'))
            typed_string = input("")
            x = self.passlen // 94
            y = self.passlen % 94
            print(colored(("".join(random.sample(self.s, 94))) * x +
                          ("".join(random.sample(self.s, y))), 'green', attrs=['bold']))
        else:
            print(colored("Yup! Good choice of password length..!!", 'yellow'))
            print(colored("".join(random.sample(self.s, self.passlen)),
                          'green', attrs=['bold']))


class MacSpoofer:
    def __init__(self):
        print(colored("hey here i will create a MacSpoofer program"), 'red')
        pass

    def changeMACadd(interface, mac):
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", mac])
        subprocess.call(["ifconfig", interface, "up"])


class ArpSpoofer:
    def __init__(self):
        print("hey here i will create a ArpSpoofer program")

    def get_target_mac(ip):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        final_packet = broadcast/arp_request
        answer = scapy.srp(final_packet, timeout=2, verbose=False)[0]
        mac = answer[0][1].hwsrc
        return mac

    def spoof_arp(target_ip, spoofed_ip):
        mac = ArpSpoofer.get_target_mac(target_ip)
        packet = scapy.ARP(op=2, hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
        scapy.send(packet, verbose=False)


class PortScanner:
    def __init__(self):
        pass

    def connScan(tgtHost, tgtPort):
        try:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect((tgtHost, tgtPort))
            print(colored(f"[+] {tgtPort}/tcp Open", 'green'))
        except:
            print(colored(f"[-] {tgtPort}/tcp Closed", 'red'))
        finally:
            sock.close()

    def portScan(tgtHost, tgtPorts):
        try:
            tgtIP = gethostbyname(tgtHost)
        except:
            print(colored(f"Unknown Host {tgtHost}", 'blue'))
        try:
            tgtName = gethostbyaddr(tgtIP)
            print(colored(f"[+] Scan Results For: {tgtName[0]} ", 'blue'))
            # print(tgtName) --> ('kali', [], ['192.168.1.8', '172.17.0.1'])
        except:
            print(colored(f"[+] Scan Results For: {tgtIP}", 'blue'))
        setdefaulttimeout(1)
        for tgtPort in tgtPorts:
            t = Thread(target=PortScanner.connScan,
                       args=(tgtHost, int(tgtPort)))
            t.start()