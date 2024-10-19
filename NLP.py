'''what is NLP ?

https://www.ibm.com/topics/natural-language-processing#:~:text=the%20next%20step-,What%20is%20natural%20language%20processing%3F,same%20way%20human%20beings%20can.

'''
'''Tokenization- https://neptune.ai/blog/tokenization-in-nlp'''

text='Welcome to the new year 2023'
x=text.split()
print(x)


#''' removing special character'''

import re
def remove_special_characters(text):
    pat=r'[^a-zA-z0-9.,!?/:;\"\'\s]'
    return re.sub(pat, '',text)
remove_special_characters("007 Not sure@ if this % was 3fun! 558923 what do you think of it.?")


#removing Numbers
import re
def remove_numbers(text):
    pattern =r'[^a-zA-z.,!?/:;\"\'\s]'
    return re.sub(pattern, '',text)
remove_numbers("007 Not sure@ if this % was 3fun! 558923 what do you think of it.?")



import re
text='Welcome to the new year 2023'
x=re.split(r'(?:,|;|\s)\s*',text)
print(x)


#'''removing punctuation'''
import string
def remove_punctuation(text):
    text= ''.join([c for c in text if c not in string.punctuation])
    return text
remove_punctuation('artical: @first sentence of same, {imporatant} ')


#'''stremaing '''
import nltk
def get_stem(text):
    stemmer = nltk.porter.PorterStemmer()
    text =' '.join([stemmer.stem(word) for word in text.split()])
    return text
get_stem("we are eating and swimming ; we have been eating and swimming ;")


import re
line = 'asdf fjdh; afed,fjek,asdf,foo'
re.split(r'(?:,|;|\s)\s*',line)


import re
text='Welcome to the new year 2023'
pattern= r'(?:,|;|\s)\s*'
x=re.split(pattern,text)
print(x)


#'''matching text at the start or end of string'''

filename='spam.txt'
filename.endswith('.ipy')
filename.endswith('.txt')


area_name='6 th lane west andheri'
area_name.endswith('west andheri')


choices=('http:','ftp:')
url='http://www.python.org'
url.endswith(choices)



#'''slicing a string'''


S ='ABCDEFGHI'
print(S[2:7])

S ='ABCDEFGHI'
print(S[-7:-2])

S ='ABCDEFGHI'
print(S[2:-5])

S ='ABCDEFGHI'
print(S[2:7:2])

S ='ABCDEFGHI'
print(S[6:1:-2])

S ='ABCDEFGHI'
print(S[:3])

S ='ABCDEFGHI'
print(S[6:])

S ='ABCDEFGHI'
print(S[::-1])


filename='spam.txt'
filename[-4:]=='.txt'

url='http://www.python.org'
url[:5]=='http:' or url[:6]=='https:' or url[:4] =='ftp'



from fnmatch import fnmatch,fnmatchcase
names=['Dat1.csv','Dat2.csv','config.int','foo']
[name for name in names if fnmatch(name,'Dat*.csv')]



from fnmatch import fnmatch,fnmatchcase
names=["andheri east","parle east","dadar west"]
[name for name in names if fnmatch(name,'*east')]



addresses =[
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
    ]
from fnmatch import fnmatch,fnmatchcase
[addr for addr in addresses if fnmatch(addr,'*ST')]


#'''Exact match'''

text = 'yeah, but no,but yeah,but no,yeah'
text=='yeah'
text.startswith('yeah')
text.endswith('no')
text.find('no')



text1 ='11/27/2012'
text2='Nov 27, 2012'
import re
if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')


#'''regular expression called regex are discription for parttern of text'''
import re
text1 ='11/27/2012'
datepat = re.compile (r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2',text1)


text ='This is artificial intelligence Era'
x=text.split()
print(x)


import re
text='india:has great history:in 2023:india is leading as its glorious fetchure! '
x=re.split(r'(?:,|:|\s)\s*',text)
print(x)


import re
text='india:has great history:in 2023:india is leading as its glorious fetchure! '
pattern= r'(?:,|;|\s)\s*'
x=re.split(pattern,text)
print(x)


import re
text='india:has great history:in 2023:india is leading as its glorious fetchure! '
x=re.split(r'(?:,|;|\s)\s*',text)
print(x)


#'''startswith and endswith provide a very basic prefix and suffix '''

text='Rama way to Haridwar to takes GangaJal'
text.endswith('Jal')

choice = ('Apple,Mango,Cherry')
choice.startswith('Apple')


#'''using string slices'''
text='I like Mango'
print(text[0:2])


import re
text ='I had  been visited pune on 11/5/2023'
if re.match(r'\d+/\d+/\d+',text):
    print('yes')
else:
    print('no')


import re
text ='11/5/2023'
if re.match(r'\d+/\d+/\d+',text):
    print('yes')
else:
    print('no')



#'''searching and replacing text'''

text = 'yeah, but no,but yeah,but no,yeah'
text.replace('yeah','ya')
text.replace('yeah','Nka yeu')


import re
text='Today is 17/05/2023 and our exam is start from 01/06/2023'
re.sub(r'(\d+)/(\d+)/(\d+)',r'(3-\1-\2)',text)


import re
text='Today is 17/05/2023 and our exam will start on 03/07/2023'
re.sub(r'(\d+)/(\d+)/(\d+)',r'(\3-\1-\2)',text)


import re
text='Today is 17/05/2023 and our exam will start on 03/07/2023'
datepat = re.compile (r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2',text)



text='Today is 17/05/2023 and our exam will start on 03/07/2023'
newtext,n=datepat.subn(r'\3-\1-\2',text)
newtext
print(n)


#'''searching and replacing case sensitive text'''
import re
text='UPPER PYTHON, LOWER PYTHON, MIXED PYTHON'
re.findall('python',text,flags=re.IGNORECASE)
re.sub('python','snake',text,flags=re.IGNORECASE)


#'''matched text''' 
import re
text='UPPER PYTHON, LOWER python, mixed PYTHON'
def matchcase(word):
    def replace(m):
        text=m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)
    


import re
str_pat= re.compile(r'\"(.*)\"')
text1='Computer says "no."'
str_pat.findall(text1)

text2='Computer says "no." phone says "yes."'
str_pat.findall(text2)

str_pat= re.compile(r'\"(.*?)\"')
str_pat.findall(text2)


import re
comment=re.compile(r'/\*(.*?)\*/')
text1='*/ this is a comment */'
comment.findall(text1)

text2='''/*this is a 
multiline comment*/'''
comment.findall(text2)

comment=re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)


#'''removing  numbers from the text'''
import re
def remove_numbers(text):
    result=re.sub(r'\d+','',text)
    return result
input_str='there are 3 balls in this bag ,and 12 in the other bag'
remove_numbers(input_str)



'''convert the numbers into words'''

import inflect
p= inflect.engine()
def convert_number(text):
    temp_str=text.split()
    new_string=[]
    for word in temp_str:
        if word.isdigit():
            temp=p.number_to_words(word)
            new_string.append(temp)
        else:
            new_string.append(word)
    temp_str=' '.join(new_string)
    return temp_str    
input_str='there are 3 balls in this bag ,and 12 in the other bag'
convert_number(input_str)  



#EXERCISE 1: Reverse each word of a string
str='my name is Vivek'
def reverse_word(sentence):
    words=sentence.split(" ")
    new_word_list=[word[::-1] for word in words]
    res_str=" ".join(new_word_list)
    return res_str
str1="my name is Vivek"
print(reverse_word(str1))

#EXERCISE 2: read the text file  into a variable and replace all new lines
with open('My.txt','r') as file:
    text = file.read().replace('\n', ' ')
    print(type(text))
    print(text)



#'''tokenization'''

import nltk
nltk.download('punkt')

def tokenize(token):
    return nltk.word_tokenize(token);
tokenize("why is this not working?");

import nltk
sentence_data = "the first sentence is about python. the second about Django.you can learn python Django and data analysis here"
nltk_tokens=nltk.sent_tokenize(sentence_data)
print(nltk_tokens)


#'''non-english tokenization'''
import nltk
german_tokenizer = nltk.data.load('tokenizers/punkt/german.pickle')
german_tokens=german_tokenizer.tokenize('wie geht es Ihnen? gut,danke.')
print(german_tokens)


#'''word tokenization'''
import nltk
word_data ="School life refers to the period of time that a person spends studying at school, typically from primary school to high school. During this time, students learn a variety of subjects, participate in extracurricular activities, and form relationships with peers and teachers."
nltk_tokens=nltk.word_tokenize(word_data)
print(nltk_tokens)


#'''engilsh stopwords'''

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stopwords.words('english')


#'''various languages'''
from nltk.corpus import stopwords
print(stopwords.fileids())



from nltk.corpus import stopwords
en_stops=set(stopwords.words('english'))
all_words=['there','is','a','tree','near','the','river']
for word in all_words:
    if word not in en_stops:
        print(word)


#'''synonyms'''
import  nltk
nltk.download('omw-1.4')
from nltk.corpus import wordnet
nltk.download('wordnet')
synonyms=[]
for syn in wordnet.synsets("Soil"): 
   for lm in syn.lemmas():
      synonyms.append(lm.name())
print(set(synonyms))


#'''antonyms'''
from nltk.corpus import wordnet
antonyms=[]
for syn in wordnet.synsets("ahead"): 
   for lm in syn.lemmas():
       if lm.antonyms():
           antonyms.append(lm.antonyms()[0].name())
print(set( antonyms))



import nltk
word_data = "The Sky is blue also the ocean is blue also Rainbow has a blue colour." 
nltk_tokens = nltk.word_tokenize(word_data)
no_order = list(set(nltk_tokens))
print(no_order)


import nltk
word_data = "The Sky is blue also the ocean is blue also Rainbow has a blue colour." 
nltk_tokens = nltk.word_tokenize(word_data)
ordered_tokens = set()
result = []
for word in nltk_tokens:
    if word not in ordered_tokens:
        ordered_tokens.add(word)
        result.append(word)
print (result) 


#To extract emails form text, we can take of regular expression

import re
text = "Please contact us at contact@xyz.com for further information."+\
        " You can also give feedbacl at feedback@xyz.com"
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print (emails)


 
import re
with open("c:/Data Science/url.txt") as file:
        for line in file:
            urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
            print(urls)

    

import string
text = 'Machine learning - advanced technology to learn'
print (string.capwords(text))
print (text.upper())


import string
text = 'Machine learning - advanced technology to learn'
transtable = text.maketrans('chd', 'abc')
print (text.translate(transtable))


import re
if  re.search("tor", "Tutorial"):
        print ("1. search result found anywhere in the string")
if re.match("Tut", "Tutorial"):
         print ("2. Match with beginning of string" )
if not re.match("tor", "Tutorial"):
        print ("3. No match with match if not beginning" )


import re
match_object = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@geekforgeeks.org')
print(match_object.group())
print(match_object.group(1))
print(match_object.group(2))
print(match_object.group(3))
print(match_object.group(1, 2, 3))


import random
import re
def replace(t):
    inner_word = list(t.group(2))
    random.shuffle(inner_word)
    return t.group(1) + "".join(inner_word) + t.group(3)
text = "Hello, You should reach the finish line."
print( re.sub(r"(\w)(\w+)(\w)", replace, text))
print (re.sub(r"(\w)(\w+)(\w)", replace, text))


str = "this is string example....wow!!! this is really string"
print (str.replace("is", "was"))


#Replacement Ignoring Case
import re
sourceline  = re.compile("Tutor", re.IGNORECASE)
 
Replacedline  = sourceline.sub("Tutor","Tutorialspoint has the best tutorials for learning.")
print (Replacedline)


#pip install pyspellchecker
from spellchecker import SpellChecker
spell = SpellChecker()
misspelled = spell.unknown(['let', 'us', 'wlak','on','the','groun'])
for word in misspelled:
    print(spell.correction(word))
    print(spell.candidates(word))

