#!/usr/bin/python3
from sys import argv


HELP_REMINDER = "type \"hjelp\" for help"
EXIT_REMINDER = "type \"tank you\" to exit"
INVALID_CMD = "ERROR: Invalid Command!"
INVALID_USAGE = "ERROR: Unexpected number of args given!"


func_dict = {}
func_descriptions = {}


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
func_dict["snus"]=snus_v1
func_descriptions["snus"]="encode to v1 snuscode"


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
func_dict["unsnus"]=unsnus_v1
func_descriptions["unsnus"]="decode from v1 snuscode"


def snus_v2(raw):
    """encode to v2 snuscode"""
    enc_int = sum([ord(c)<<(i*7) for i,c in enumerate(raw[::-1])])
    enc = ""
    while enc_int != 0:
        enc_int, rem = divmod(enc_int, 3)
        enc += "snu"[rem]
    return enc
func_dict["neosnus"]=snus_v2
func_descriptions["neosnus"]="encode to v2 snuscode"


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
func_dict["unneosnus"]=unsnus_v2
func_descriptions["unneosnus"]="decode from v2 snuscode"


def print_help(*_):
    for func, desc in func_descriptions.items():
        print(func.ljust(12) + " - " + desc )
func_dict["hjelp"]=print_help
func_descriptions["hjelp"]="show help for this script"


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
        except KeyError:
            print(INVALID_CMD)
            print(HELP_REMINDER)
            print(EXIT_REMINDER)


def main():
    if len(argv) == 1:
        interactive_snus()
    else:
        cmd, msg = argv[1], " ".join(argv[2:])
        try:
            if(ret:=func_dict[cmd](msg)) != None:
                print(ret)
        except KeyError:
            print(INVALID_CMD)
            print(f"usage: {argv[0]} <cmd> <msg>")
            print(HELP_REMINDER)
    
if __name__ == "__main__":
    main()
