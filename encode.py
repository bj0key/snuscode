import const

def snus_legacy(msg):
    """encode to legacy snuscode"""
    enc = ""
    for c in msg:
        # For each char, encode into a 5-digit ternary 'number'
        n = ord(c)
        w = ""
        for i in range(5):
            d, r = divmod(n, 3)
            w += "snu"[r]
            n = d
        enc += w[::-1]
    return(enc)


def snus_rev2(msg):
    """encode to revision 2 snuscode"""
    enc_int = sum([ord(c)<<(i*7) for i,c in enumerate(msg[::-1])])
    enc = "ssss"
    while enc_int != 0:
        enc_int, rem = divmod(enc_int, 3)
        enc += "snu"[rem]
    return enc

encode_format = {"legacy":snus_legacy, "rev2":snus_rev2}

def encode(msg, fmt="auto"):
    fmt = "rev2" if fmt=="auto" else fmt
    try:
        return encode_format[fmt](msg)
    except KeyError:
        print(const.UKNOWN_FORMAT)
        return