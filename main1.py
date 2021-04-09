#!/usr/bin/python3

'''
C-Caeser Cipher
S-Strong password generator
M-Mac Spoofer
A-Arp scanner
P-port scanner
This will be a command line project with some web interface that may be run on localhost.
'''

'''
To-Do list:-
# I have to create a decrypt algo and there should be concept of symmetric key. --> done
# I have to create a caeser cipher tool in web site
# I have to create an advance port scanner.
# Add some more features in ARP spoofer.
# Design and add text in html.
# May add some features which use to fetch data from database and display on the website.

'''


import argparse
import sys
import os
import string
import optparse
import random
from termcolor import colored
from time import sleep
import webapp
from modules import *

helper = colored('''
Caeser Cipher:
    csmap -c <text> -k <key> 
Password Generator:
    csmap -l <length of password>
Port Scanner:
    csmap -p <port no.> <ip address>
MAC Spoofer:
    csmap -cyan
ARP Spoofer:
    sudo csmap -a <router ip> -v <victim ip>''', 'cyan')



if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=helper)
    fPlace = sys.argv
    try:
        if '-c' in fPlace:
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

        elif '-d' in fPlace:
            print("this is for decrypting cipher")
            parser.add_argument('-d', type=str,
                                default=None,
                                help='csmap -c <text> -k <key> ')
            parser.add_argument('-k', type=int,
                                default=None,
                                help='csmap -c <text> -k <key> ')
            args = parser.parse_args()
            # val=sys.stdout.write(str(c.encrypt()))
            c = CaeserCipher(args.d, args.k)
            val = c.decrypt()
            print(colored(f"Text: \'{args.d}\' ", 'yellow'))
            print(
                colored(f"Caeser Cipher Text: \'{val}\' ", 'green', attrs=['bold']))

        elif '-l' in fPlace:
            parser.add_argument('-l', type=int,
                                default=None,
                                help='csmap -l <length of password>')
            args = parser.parse_args()
            PassGenerator(args.l)

        elif '-p' in fPlace:
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

        elif '-m' in fPlace:
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

        elif 'help' in fPlace:
            if 'web' in fPlace:
                webapp.app.run(host="127.0.0.1", port=8080, debug=True)
            else:
                print("Usage"+helper)

        elif '-a' in fPlace:
            parser.add_argument(
                '-a', type=str, default="192.168.1.1", help="ip of router")
            parser.add_argument(
                '-v', type=str, default=None, help="ip of victim")
            args = parser.parse_args()
            try:
                while True:
                    ArpSpoofer.spoof_arp(args.a, args.v)
                    ArpSpoofer.spoof_arp(args.v, args.a)
                    # ArpSpoofer.spoof_arp("192.168.1.1","192.168.1.3")
                    # spoof_arp("ip_of_router","ip_of_victim")
                    # spoof_arp("ip_of_victim","ip_of_router")

            except KeyboardInterrupt:
                print(colored("\n[-] Stopping!!", "red"))
                sleep(2)

            except:
                print(
                    colored("Some Error Occured , first ping the victim computer", 'red'))
        else:
            print("Usage:"+helper)
    except KeyboardInterrupt:
        print(colored(helper, 'cyan'))
