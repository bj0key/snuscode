#!/usr/bin/python3
from sys import argv

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
      

def main():
    if len(argv) > 2 and argv[1] == "snus":
        snus(" ".join(argv[2:]))
    elif len(argv) > 2 and argv[1] == "unsnus":
        unsnus(" ".join(argv[2:]))
    else:
        print("ERROR: Invalid args given!")
        print("Usage: ./snus.py [snus/unsnus] [msg]")
    
if __name__ == "__main__":
    main()
