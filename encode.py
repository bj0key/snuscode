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


def snus_rev2_rle(msg):
    """Encode to rev2 snus, but then perform
       a primitie RLE using exclusively s, n, and u"""
    rev2 = snus_rev2(msg)[4:] # remove the "ssss" from the beginning (redundant)
    last_char = None
    run_length = 0 #run length
    enc = "sssS"
    for c in rev2:
        if run_length>3 or (last_char!=c and last_char!=None):
            enc += last_char
            if run_length>2: enc+="SNU"[run_length-3]
            elif run_length == 2: enc+=last_char
            run_length = 0
        last_char = c
        run_length+=1
    enc += last_char
    if run_length>2: enc+="SNU"[run_length-3]
    elif run_length == 2: enc+=last_char
    return enc


encode_format = {"legacy":snus_legacy, "rev2":snus_rev2, "rev2-rle":snus_rev2_rle}

def encode(msg, fmt="auto"):
    fmt = "rev2" if fmt=="auto" else fmt
    try:
        return encode_format[fmt](msg)
    except KeyError:
        print(const.INVALID_FORMAT)
        return