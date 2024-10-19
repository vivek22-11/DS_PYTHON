

#'''normalizing unicode text to standard represenation'''

s1= 'Spicy Jalape\u00f1o'
s2= 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
s1==s2


#'''normalization from of canonical composition'''

import unicodedata
s1= 'Spicy Jalape\u00f1o'
s2= 'Spicy Jalapen\u0303o'
t1=unicodedata.normalize('NFC',s1) 
t2=unicodedata.normalize('NFC',s2)
t1==t2
print(ascii(t1))


import unicodedata
s1= 'Spicy Jalape\u00f1o'
s2= 'Spicy Jalapen\u0303o'
t3=unicodedata.normalize('NFD',s1)
t4=unicodedata.normalize('NFD',s2)
t3==t4
print(ascii(t3))


import unicodedata
s1= 'Spicy Jalape\u00f1o'
t1=unicodedata.normalize('NFD',s1)
''.join(c for c in t1 if not unicodedata.combining(c))



#'''unicode character in regular expression'''
import re
num=re.compile('\d+')
#ASCII digits
num.match('123')
pat=re.compile('stra\u00dfe',re.IGNORECASE)
s='strße'
pat.match(s)
pat.match(s.upper())
s.upper()


#'''stripping unwanted characters from strings lstrip() and rstrip()'''


s='  hello word\n'
s.strip()
s.lstrip()
s.rstrip()


#'''character stripping'''

t='-------hello==========='
t.lstrip('-')
t.strip('-=')

s='  hello word    \n'
s=s.strip()
s
s.replace(' ','')


import re
re.sub('\s+',' ',s)
'hello word'



s = 'pýtĥöñ\fis\tawesome\r\n'
s
remap={
       ord('\t'):' ',
       ord('\f'):' ',
       ord('\r'): None 
       }
a=s.translate(remap)
a



s = 'pýtĥöñ\fis\tawesome\r\n'
s
remap={
       ord('\t'):' ',
       ord('\f'):' ',
       ord('\n'):' ',
       ord('\r'): None #deleted
       }
a=s.translate(remap)
a


import unicodedata
import sys
cmb_chrs=dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b=unicodedata.normalize('NFD', a)
b
b.translate(cmb_chrs)


a='pýtĥöñ is awesome\n'
b=unicodedata.normalize('NFD',a)
b.encode('ascii', 'ignore').decode('ascii')


#'''aligning the text string'''

text='Hello World'
text.ljust(20)
text.rjust(20)
text.center(20)
text.rjust(20,'=')
text.center(20,'*')
format(text,'>20')
format(text,'<20')
format(text,'^20')
format(text,'=>20s')
format(text,'*^20s')
'{:>10s} {:>10s}'.format('hello', 'world')



x = 1.2345
format(x,'>10')
format(x, '^10.2f')


parts = ['Is','Chicago','Not','Chicago']
','.join(parts)

parts = ['Is','Chicago','Not','Chicago']
''.join(parts)


a = 'Is Chicago'
b = 'not Chicago'
print('{} {}'.format(a,b))


a='Hello' 'World'
a


a='Hello'' ''World'
a


s='{name} has {n} messages'
s.format(name='Dnyaneshwari',n=42)


s='{name} has {n} messages'
name='Dnyaneshwari'
n=42
s.format_map(vars())


import textwrap
s='1. The Clearance form, for submission has, been created for the students. \
Student need ,to collect the form from ,class coordinator\
Students have to, take the signature of the class, coordinator and \
'
print(textwrap.fill(s,70,initial_indent=' '))


import textwrap
s='1. The Clearance form, for submission has, been created for the students. \
Student need ,to collect the form from ,class coordinator\
Students have to, take the signature of the class, coordinator and \
'
print(textwrap.fill(s,70,subsequent_indent=' '))




class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
        
a = Info('Guido',37)
s.format_map(vars(a))

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
import textwrap
print(textwrap.fill(s, 70))

print(textwrap.fill(s, 40))

print(textwrap.fill(s, 40, initial_indent=' '))

print(textwrap.fill(s, 40, subsequent_indent=' '))



s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))



# Disable escaping of quotes
print(html.escape(s, quote=False))
from html.parser import HTMLParser
p = HTMLParser()
p.unescape(s)

