### Este archivo define las funciones para printear con colores en la terminal

class colors:
    HEADER    = '\033[95m'
    BLUE      = '\033[94m'
    CYAN      = '\033[96m'
    GREEN     = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'

def blue(string):
    return colors.BLUE + string + colors.ENDC

def cyan(string):
    return colors.CYAN + string + colors.ENDC

def green(string):
    return colors.GREEN + string + colors.ENDC

def header(string):
    return colors.HEADER + string + colors.ENDC

def yellow(string):
    return colors.WARNING + string + colors.ENDC