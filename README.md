#[Project CSMAP](http://127.0.0.1:8080 "CSMAP")

# CSMAP

**CSMAP is an integrated tool which provides you many facilities and help you in Pentesting,Networking and Bug Hunting.**


This projects includes multiple tools which are as follows:

- Caeser Cipher
- Strong Password Generator
- MAC Spoofer
- ARP Spoofer
- Port Scanner

**Installation:**
`pip install -r requirements.txt`

If permission denied then use:
`sudo pip install -r requirements.txt`

**Usage:**

1. Caeser Cipher:

- Encrypt The Plain Text:
`sudo python3 csmap.py -c <plain text> -k <key>`

- Decrypt The Cipher Text:
`sudo python3 csmap.py -d <cipher text> -k <key>`

2. Strong Password Generator:

    `sudo python3 csmap.py -l <length of password>`

3. MAC Spoofer:

    `sudo python3 csmap.py -m`

4. ARP Spoofer:

    `sudo python3 csmap.py -a <router ip> -v <victim ip>`

5. Port Scanner

    `sudo python3 csmap.py -p <port no.> <ip address>`