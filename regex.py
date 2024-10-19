

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfReader
reader=PdfReader('C:\Data Science\Literature Review.pdf')
#print number of pages
print(len(reader.pages))
#getting a specific page from the pdf file
page =reader.pages[3]
text=page.extract_text()
print(text)

###############################################################################
'''https://regex101.com/'''

import re
chat1="Hii my order #496724 is not received yet"
chat2='Hii,I having a problem with my order number 41288912,which is  not recived'
chat3='Hii my order 496724 is having an issue'
pattern='order[^\d]*(\d*)'
order=re.findall(pattern,chat1)
print(order)
order=re.findall(pattern,chat2)
print(order)
order=re.findall(pattern,chat3)
print(order)

###############################################################################
import re
text1="My Phone Number is 7249042768"
text2="My alternate Phone number is 8600136830"
text3="my international phone number(124)-234-23432"
pat1='\d{10}'
#pat2='(?:.....)-\d{3}-\d{5}'
pat2='\(\d{3}\)\-\d{3}-\d{5}'
ph_num1=re.findall(pat1,text1)
print(ph_num1)
ph_num2=re.findall(pat1,text2)
print(ph_num2)
ph_num3=re.findall(pat2,text3)
print(ph_num3)

###############################################################################
import re
pat1='/[a-z_A-Z0-9]*@[a-z]*\.com'
text1="My Email Id is vivekkadam082@gmail.com"
text2="My alternate Emial Id is vivekkadam000@gmail.com"
text3="my Official Mail Id is vivekkadamofficial@gmail.com"
pat2='[a-z]*\.[a-z_A-Z0-9]*@[a-z]*\.[a-z]*\.in'
text4="vivek.kadam@sanjivani.org.in"

email=re.findall(pat1,text1)
print(email)


###############################################################################
import re
chat1=' Hello, I am having an issue with my order #412889912'
pattern='order[^\d]*(\d*)'
order=re.findall(pattern,chat1)
print(order)


chat1=' Hello, I am having an issue with my order #412889912'
def get_pattern_match(pattern, text):
    matches=re.findall(pattern, text)
    if matches:
        return matches
get_pattern_match('order[^\d]*(\d*)', chat1)


#Retrieve email id and phone
chat1='hi: you ask lot of question 1234567891, abc@xyz.com'
chat2='hi: here it is : (123)-567-8912, abc@xyz.com'
chat3='hi:yes,phone: 1234567891 email:abc@xyz.com'

get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat2)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat3)

#phone number
get_pattern_match('(\d{10})|(\(\d{3}\)\-\d{3}-\d{4})',chat3)
get_pattern_match('(\d{10})|(\(\d{3}\)\-\d{3}-\d{4})',chat3)
get_pattern_match('(\d{10})|(\(\d{3}\)\-\d{3}-\d{4})',chat3)



###############################################################################
text='''Born	Elon Reeve Musk
June 28, 1971 (age 51)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and chairman of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp. and X.AI
Co-founder of Neuralink, OpenAI, Zip2 and X.com (part of PayPal)'''
get_pattern_match(r'age (\d+)', text)
get_pattern_match(r'Born(.*)', text)
match=get_pattern_match(r'Born(.*)', text)
match[0].strip()
match=get_pattern_match(r'Born.*\n(.*)\(age', text)                                               
match[0].strip()
get_pattern_match(r'\(age.*\n(.*)', text)



###############################################################################
text='''Born	Elon Reeve Musk
June 28, 1971 (age 51)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and chairman of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp. and X.AI
Co-founder of Neuralink, OpenAI, Zip2 and X.com (part of PayPal)'''

def extract_personal_information(text):
    age = get_pattern_match('age (\d+)', text)
    full_name = get_pattern_match('Born(.*)\n', text)
    birth_date = get_pattern_match('Born.*\n(.*)\(age', text)
    birth_place = get_pattern_match('\(age.*\n(.*)', text)
    return{
        'age':age,
        'name':full_name,
        'birth_date':birth_date,
        'birth_place':birth_place
        }
extract_personal_information(text)



###############################################################################
text1='''Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 66)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parent	
Dhirubhai Ambani (father)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)'''
get_pattern_match(r'age (\d+)', text1)
get_pattern_match(r'Born(.*)', text1)
match=get_pattern_match(r'Born(.*)', text1)
match[0].strip()
match=get_pattern_match(r'Born.*\n(.*)\(age', text1)                                               
match[0].strip()
get_pattern_match(r'\(age.*\n(.*)', text1)



###############################################################################
text1='''Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 66)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parent	
Dhirubhai Ambani (father)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)'''
def extract_personal_information(text1):
    age = get_pattern_match('age (\d+)', text1)
    full_name = get_pattern_match('Born(.*)\n', text1)
    birth_date = get_pattern_match('Born.*\n(.*)\(age', text1)
    birth_place = get_pattern_match('\(age.*\n(.*)', text1)
    return{
        'age':age,
        'name':full_name,
        'birth_date':birth_date,
        'birth_place':birth_place
        }
extract_personal_information(text1)



###############################################################################
text='''Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''
pattern= 'https://twitter\.com/([a-zA-Z0-9_]+)'
re.findall(pattern, text)


###############################################################################
text='''Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, 
cash equivalents, marketable securities,restricted cash, accounts receivable, convertible note hedges, 
and interest rate swaps. 
Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are 
typically in excess of insured limits. As of September 30, 2021 and December 31,'''

pattern='Concentration of Risk: ([^\n]*)'
re.findall(pattern, text)


###############################################################################
text=''''Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.'''
pattern = 'FY(\d{4} (?:Q[1-4]|S[1-2]))'
matches= re.findall(pattern, text)
print(matches)


###############################################################################
test='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern='\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches= re.findall(pattern, text)
print(matches)


###############################################################################
text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''
pattern= 'Note \d - ([^\n]*)'
matches= re.findall(pattern, text)
print(matches)


###############################################################################
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern= 'FY\d{4} Q[1-4]'
matches= re.findall(pattern, text)
print(matches)

###############################################################################
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''
pattern= 'FY\d{4} Q[1-4]'
matches= re.findall(pattern, text,flags=re.IGNORECASE)
print(matches)

###############################################################################

text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern= '\$([0-9\.]+)'
matches= re.findall(pattern, text)
matches

