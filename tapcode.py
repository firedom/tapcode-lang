import os, sys

def pikalang(str):
    str = str.lower()
    output = ''
    for s in str:
        if s == 'a':
            output += '·· ·/'
            continue
        if s == 'b':
            output += '· ····/'
            continue
        if s == 'c':
            output += '· ·· ··/'
            continue
        if s == 'd':
            output += '· ···/'
            continue
        if s == 'e':
            output += '··/'
            continue
        if s == 'f':
            output += '··· ··/'
            continue
        if s == 'g':
            output += '· · ··/'
            continue
        if s == 'h':
            output += '·····/'
            continue
        if s == 'i':
            output += '···/'
            continue
        if s == 'j':
            output += '·· · · ·/'
            continue
        if s == 'k':
            output += '· ·· ·/'
            continue
        if s == 'l':
            output += '·· ···/'
            continue
        if s == 'm':
            output += '· · ·/'
            continue
        if s == 'n':
            output += '· ··/'
            continue
        if s == 'o':
            output += '· · · ·/'
            continue
        if s == 'p':
            output += '·· · ··/'
            continue
        if s == 'q':
            output += '· · ·· ·/'
            continue
        if s == 'r':
            output += '·· ··/'
            continue
        if s == 's':
            output += '····/'
            continue
        if s == 't':
            output += '· ·/'
            continue
        if s == 'u':
            output += '··· ·/'
            continue
        if s == 'v':
            output += '···· ·/'
            continue
        if s == 'w':
            output += '·· · ·/'
            continue
        if s == 'x':
            output += '· ··· ·/'
            continue
        if s == 'y':
            output += '· ·· · ·/'
            continue
        if s == 'z':
            output += '· · ···/'
            continue
        if s == '0':
            output += '· · · · · ·/'
            continue
        if s == '1':
            output += '·· · · · ·/'
            continue
        if s == '2':
            output += '··· · · · ·/'
            continue
        if s == '3':
            output += '···· · ·/'
            continue
        if s == '4':
            output += '····· ·/'
            continue
        if s == '5':
            output += '······/'
            continue
        if s == '6':
            output += '· ·····/'
            continue
        if s == '7':
            output += '· · ····/'
            continue
        if s == '8':
            output += '· · · ···/'
            continue
        if s == '9':
            output += '· · · · ··/'
            continue
        if s == ' ':
            output += ' /'
            continue
        output += s

    return output

if __name__ == "__main__":
    if len(sys.argv) <= 1 or  len(sys.argv) >= 3:
        print("""invalid input.

If you want translate words, input:
python3 tapcode.py nyanya~
The Terminal will return:
· ··/· ·· · ·/·· ·/· ··/· ·· · ·/·· ·/~

Or translate sentence, input:
python3 tapcode.py "Author by firedom"
The Terminal will return:
·· ·/··· ·/· ·/·····/· · · ·/·· ··/ /· ····/· ·· · ·/ /··· ··/···/·· ··/··/· ···/· · · ·/· · ·/""")
        sys.exit(0)
    print(pikalang(sys.argv[1]))
