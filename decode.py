import const

strip_prefix = lambda m, p: m[4:] if m[0:4]==p else m

def unsnus_legacy(msg):
    """decode from v1 snuscode"""
    dec = ""
    clusters = [str(msg[i:i+5]) for i in range(0, len(msg), 5)]
    for c in clusters:
        n = 0
        for i in c:
            n*=3
            try:
                n+="snu".index(i)
            except ValueError:
                print(const.ILLEGAL_CHARS)
                return
        dec += chr(n)
    return(dec)


def unsnus_rev2(msg):
    """decode from v2 snuscode"""
    msg = strip_prefix(msg, "ssss")
    try:
        enc_int = sum([int("snu".index(c) * int(3**i)) for i,c in enumerate(msg)])
    except ValueError:
        print(const.ILLEGAL_CHARS)
        return ""
    msg_b = bin(enc_int)[2:]
    chr_b = [msg_b[i:i+7] for i in range(0,len(msg_b),7)]
    return "".join([chr(int(c,2)) for c in chr_b])


def unsnus_rev2_rle(msg):
    """Decodes a variant upon rev2 snus, in which capital letters denote same-char runs"""
    msg = strip_prefix(msg, "sssS")
    exp = "" # expanded msg to send to 
    for c in msg:
        if c in "snu": # same-value
            exp += c
            l = c
        elif c in "SNU": # repeat last char 2/3/4 times
            exp += l * ("SNU".index(c)+2)
        else:
            print(c)
            raise ValueError("Unexpected character found")
    return unsnus_rev2(exp)


encode_formats = {"legacy":unsnus_legacy, "rev2":unsnus_rev2, "rev2-rle":unsnus_rev2_rle}
encode_prefixes = {"ssss":"rev2", "sssS":"rev2-rle"}

def decode(msg, fmt="auto"):
    if fmt == "auto":
        if msg[0]!="s":
            fmt = "legacy"
        else:
            fmt = encode_prefixes[msg[0:4]]
            msg = msg[4:]
            
    try:
        return encode_formats[fmt](msg)
    except KeyError:
        print(const.INVALID_FORMAT)
        return