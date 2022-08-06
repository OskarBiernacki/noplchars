from os.path import exists
import sys

chang = {
        'ą' : 'a',
        'ć' : 'c',
        'ę' : 'e',
        'ł' : 'l',
        'ń' : 'n',
        'ó' : 'o',
        'ś' : 's',
        'ź' : 'z',
        'ż' : 'z'
        }

print("python noplchars.py <FILENAME>")
FILE = sys.argv[1]
OUT_FILE = 'nopl_' + FILE
if exists(FILE) == False:
    print(FILE + "is not exist")
    exit()
open(OUT_FILE, 'w').write("")
for line in open(FILE, 'r'):
    newLine=''
    for i in line:
        try:
            newLine += chang[i.lower()]
        except:
            newLine += i
    open(OUT_FILE, 'a').write(newLine)

print("Finish")
