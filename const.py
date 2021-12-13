VALID_FORMATS = ["auto", "legacy", "rev2"]

HELP_REMINDER = "type \"hjelp\" for help"
EXIT_REMINDER = "type \"tank you\" to exit"

INTERACTIVE_HELP = """Available commands:
     snus - encode a message
   unsnus - decode a messsage
setformat - set the encoding format
  formats - list available formats
    hjelp - print this message
 tank you - exit interactive prompt"""

INVALID_CMD = "ERROR: Invalid Command!"
FORMAT_SUCCESS = "Successfully set format to"
INVALID_FORMAT = "ERROR: Invalid Format!\nTry using \"formats\" to list all available formats"
INVALID_USAGE = "ERROR: Unexpected number of args given!"

ILLEGAL_CHARS = "ERROR: Illegal characters in message! Unable to decode"
DECODE_FAILURE = "ERROR: Unknown format!\nPerhaps try manually specifying encoding with -fmt [fmt]"