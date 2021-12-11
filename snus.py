#!/usr/bin/python3
from sys import argv

USAGE_MSG = """Usage: [snus/unsnus] [message]
\"tank you\" to exit"""



def snus(raw):
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
    print(enc)

def unsnus(enc):
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
    print(raw)

def interactive_snus():
    print("snuscode interactive prompt")
    print(USAGE_MSG)
    while(True):
        while (inp:=input(">>> ").split(" "))[0] not in ["snus", "unsnus"] and " ".join(inp[0:2])!="tank you":
            print("invalid command!")
            print(USAGE_MSG)
        if inp[0]=="help":
            print(USAGE_MSG)
        elif inp[0]=="snus":
            snus(" ".join(inp[1:]))
        elif inp[0]=="unsnus":
            unsnus(" ".join(inp[1:]))
        elif " ".join(inp[0:2]) == "tank you":
            return

    
def main():
    if len(argv) == 1:
        interactive_snus()
    elif len(argv) > 2 and argv[1] == "snus":
        snus(" ".join(argv[2:]))
    elif len(argv) > 2 and argv[1] == "unsnus":
        unsnus(" ".join(argv[2:]))
    else:
        print("ERROR: Invalid args given!")
        print(f"Usage: {argv[0]} [snus/unsnus] [msg]")
    
if __name__ == "__main__":
    main()
