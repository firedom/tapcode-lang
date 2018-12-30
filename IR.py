import os, sys

def pikalang(str):
    str = str.lower()
    temp= ''
    output = ''
    for s in str:
        if s == '·':
            temp += s
            continue
        if s == ' ':
            temp += s
            continue
        if s == '/':
            temp += s
            if temp == '·· ·/':
                output += 'a'
                temp = ''
                continue
            if temp == '· ····/':
                output += 'b'
                temp = ''
                continue
            if temp == '· ·· ··/':
                output += 'c'
                temp = ''
                continue
            if temp == '· ···/':
                output += 'd'
                temp = ''
                continue
            if temp == '··/':
                output += 'e'
                temp = ''
                continue
            if temp == '··· ··/':
                output += 'f'
                temp = ''
                continue
            if temp == '· · ··/':
                output += 'g'
                temp = ''
                continue
            if temp == '·····/':
                output += 'h'
                temp = ''
                continue
            if temp == '···/':
                output += 'i'
                temp = ''
                continue
            if temp == '·· · · ·/':
                output += 'j'
                temp = ''
                continue
            if temp == '· ·· ·/':
                output += 'k'
                temp = ''
                continue
            if temp == '·· ···/':
                output += 'l'
                temp = ''
                continue
            if temp == '· · ·/':
                output += 'm'
                temp = ''
                continue
            if temp == '· ··/':
                output += 'n'
                temp = ''
                continue
            if temp == '· · · ·/':
                output += 'o'
                temp = ''
                continue
            if temp == '·· · ··/':
                output += 'p'
                temp = ''
                continue
            if temp == '· · ·· ·/':
                output += 'q'
                temp = ''
                continue
            if temp == '·· ··/':
                output += 'r'
                temp = ''
                continue
            if temp == '····/':
                output += 's'
                temp = ''
                continue
            if temp == '· ·/':
                output += 't'
                temp = ''
                continue
            if temp == '··· ·/':
                output += 'u'
                temp = ''
                continue
            if temp == '···· ·/':
                output += 'v'
                temp = ''
                continue
            if temp == '·· · ·/':
                output += 'w'
                temp = ''
                continue
            if temp == '· ··· ·/':
                output += 'x'
                temp = ''
                continue
            if temp == '· ·· · ·/':
                output += 'y'
                temp = ''
                continue
            if temp == '· · ···/':
                output += 'z'
                temp = ''
                continue
            if temp == '· · · · · ·/':
                output += '0'
                temp = ''
                continue
            if temp == '·· · · · ·/':
                output += '1'
                temp = ''
                continue
            if temp == '··· · · ·/':
                output += '2'
                temp = ''
                continue
            if temp == '···· · ·/':
                output += '3'
                temp = ''
                continue
            if temp == '····· ·/':
                output += '4'
                temp = ''
                continue
            if temp == '······/':
                output += '5'
                temp = ''
                continue
            if temp == '· ·····/':
                output += '6'
                temp = ''
                continue
            if temp == '· · ····/':
                output += '7'
                temp = ''
                continue
            if temp == '· · · ···/':
                output += '8'
                temp = ''
                continue
            if temp == '· · · · ··/':
                output += '9'
                temp = ''
                continue
            if temp == ' /':
                output += ' '
                temp = ''
                continue
        output += s

    
    return output

if __name__ == "__main__":
    if len(sys.argv) <= 1 or  len(sys.argv) >= 3:
        print("""invalid input.
            
If you want translate words, input:
python3 IR.py "· ··/· ·· · ·/·· ·/· ··/· ·· · ·/·· ·/~"
The Terminal will return:
nyanya~
            
Or translate sentence, input:
python3 IR.py "·· ·/··· ·/· ·/·····/· · · ·/·· ··/ /· ····/· ·· · ·/ /··· ··/···/·· ··/··/· ···/· · · ·/· · ·/"
The Terminal will return:
author by firedom""")
        sys.exit(0)
    print(pikalang(sys.argv[1]))

