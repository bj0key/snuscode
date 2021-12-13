import const

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
    if msg[0:4]=="ssss": msg=msg[4:]
    try:
        enc_int = sum([int("snu".index(c) * int(3**i)) for i,c in enumerate(msg)])
    except IndexError:
        print("ERROR: Invalid encoding! Unable to unsnus")
        return ""
    msg_b = bin(enc_int)[2:]
    chr_b = [msg_b[i:i+7] for i in range(0,len(msg_b),7)]
    return "".join([chr(int(c,2)) for c in chr_b])

encode_format = {"legacy":unsnus_legacy, "ssss":unsnus_rev2}

def decode(msg, fmt="auto"):
    if fmt == "auto":
        if msg[0]!="s":
            fmt = "legacy"
        else:
            fmt = msg[0:4]
            msg = msg[4:]
            
    try:
        return encode_format[fmt](msg)
    except KeyError:
        print(const.UKNOWN_FORMAT)
        return