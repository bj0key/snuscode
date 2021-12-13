#!/usr/bin/python3
from sys import argv
import argparse

parser = argparse.ArgumentParser(usage='<command> " the message you want "')
parser.add_argument('-snus', help='encode to v1 snuscode', nargs='+', metavar='')
parser.add_argument('-unsnus', help='decode from v1 snuscode', nargs='+', metavar='')
parser.add_argument('-neosnus', help='encode to v2 snuscode', nargs='+', metavar='')
parser.add_argument('-unneosnus', help='decode from v2 snuscode', nargs='+', metavar='')

args = parser.parse_args()
raw = args.snus, args.neosnus
enc = args.unsnus, args.unneosnus

HELP_REMINDER = "type \"hjelp\" for help"
EXIT_REMINDER = "type \"tank you\" to exit"
INVALID_CMD = "ERROR: Invalid Command!"
INVALID_USAGE = "ERROR: Unexpected number of args given!"

def snus_v1(raw):
    """encode to v1 snuscode"""
    enc = ""
    for c in raw:
        # For each char, encode into a 5-digit ternary 'number'
        n = ord(c)
        w = ""
        for i in range(5):
            d, r = divmod(n, 3)
            w += "snu"[r]
            n = d
        enc += w[::-1]
    return(enc)

def unsnus_v1(enc):
    """decode from v1 snuscode"""
    raw = ""
    chunks = [str(enc[i:i+5]) for i in range(0, len(enc), 5)]
    for c in chunks:
        n = 0
        for i in c:
            n*=3
            try:
                n+="snu".index(i)
            except ValueError:
                print("ERROR: Invalid encoding! Unable to unsnus")
                return
        raw += chr(n)
    return(raw)

def snus_v2(raw):
    """encode to v2 snuscode"""
    enc_int = sum([ord(c)<<(i*7) for i,c in enumerate(raw[::-1])])
    enc = ""
    while enc_int != 0:
        enc_int, rem = divmod(enc_int, 3)
        enc += "snu"[rem]
    return enc

def unsnus_v2(enc):
    """decode from v2 snuscode"""
    try:
        enc_int = sum([int("snu".index(c) * int(3**i)) for i,c in enumerate(enc)])
    except IndexError:
        print("ERROR: Invalid encoding! Unable to unsnus")
        return
    msg_b = bin(enc_int)[2:]
    chr_b = [msg_b[i:i+7] for i in range(0,len(msg_b),7)]
    msg = "".join([chr(int(c,2)) for c in chr_b])
    return msg

def print_help(*_):
    for func, desc in func_descriptions.items():
        print(func.ljust(12) + " - " + desc )

func_dict = {"snus":snus_v1, "unsnus":unsnus_v1, "neosnus":snus_v2, "unneosnus":unsnus_v2}

def interactive_snus():
    print("snuscode interactive prompt v2.0")
    print(HELP_REMINDER)
    print(EXIT_REMINDER)
    while(True):
        inp=input(">>> ").split(" ")
        cmd,msg = inp[0], " ".join(inp[1:])
        
        if " ".join(inp[0:2]) == "tank you": return
        try:
            if(ret:=func_dict[cmd](msg)) != None:
                print(ret)
        except IndexError:
            print("poop")

if args.snus:
	print(snus_v1(' '.join(args.snus)))
elif args.unsnus:
	print(unsnus_v1(' '.join(args.unsnus)))
elif args.neosnus:
	print(snus_v2(' '.join(args.neosnus)))
elif args.unneosnus:
	print(unsnus_v2(' '.join(args.unneosnus)))
if len(argv) == 1:
	interactive_snus()
