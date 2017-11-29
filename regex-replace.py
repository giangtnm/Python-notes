#!/usr/bin/python
import re

i = "abc123\n\n123abc\n\ndef456\n\n\n\n456def"
print i
print "*******************************************"

def loop_replace():
    a = i
    while '\n\n' in a:
        a = a.replace('\n\n', '\n')
    print a

loop_replace()

print "*******************************************"

b = re.sub(r'([\n]+)', r'\n', i)

print b

'''result
abc123

123abc

def456



456def
*******************************************
abc123
123abc
def456
456def
*******************************************
abc123
123abc
def456
456def
'''

