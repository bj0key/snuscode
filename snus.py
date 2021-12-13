#!/usr/bin/python3
from sys import argv
import encode, decode, argparse, const


def interactive_snus():
    cmds_dict = {
        "snus" : encode.encode,
        "unsnus": decode.decode,
        "hjelp": lambda cmd,msg: const.INTERACTIVE_HELP
    }
    format = args.format
    print("snuscode interactive prompt v2.0")
    print(const.HELP_REMINDER)
    print(const.EXIT_REMINDER)
    while(True):
        inp = input(">>> ").split()
        cmd, message = inp[0], " ".join(inp[1:])
        if " ".join(inp[0:2]) == "tank you":
            return
        
        elif cmd == "setformat":
            if message in const.VALID_FORMATS:
                format = message
                print(FORMAT_SUCCESS, format)
            else:
                print(const.INVALID_FORMAT)
                
        elif cmd == "formats":
            print("Available Formats:")
            [print(f) for f in const.VALID_FORMATS]
            
        elif cmd in cmds_dict:
            print(cmds_dict[cmd](message, format))
            
        else:
            print(const.INVALID_CMD)


def main():
    message = " ".join(args.message)
    if args.message == "":
        interactive_snus()
    elif args.mode == "snus":
        print(encode.encode(message, args.format))
    elif args.mode == "unsnus":
        print(decode.decode(message, args.format))


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("message", help="The message to be encoded/decoded", nargs="+")
    parser.add_argument('-mode', help='Specify whether to encode or decode msg', default="snus", choices=("snus", "unsnus"))
    parser.add_argument("-format", help="Specify the format to use", nargs="?", default="auto", choices=const.VALID_FORMATS)
    args = parser.parse_args()  
    main()
