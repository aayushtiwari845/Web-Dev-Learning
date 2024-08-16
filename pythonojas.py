
import spacy
from pdfminer.high_level import extract_text
import re
import os
import pandas as pd 

Path=r"C:\\ojaspdf"

print(Path)
file=[f for f in os.listdir(Path) if f.endswith('.pdf')]
print(file)

nlp= spacy.load("en_core_web_sm")

result_dict={'Name':[],'Mobile_Number':[],'Email_Id':[],'Vehicle_no':[],'Policy_no':[],'Policy_start_dt':[],'Policy_end_dt':[]}
print(result_dict)

Name = []
Mobile_Number= []
Email_Id= [] 
Vehicle_no= [] 
Policy_no= [] 
Policy_start_dt=  [] 
Policy_end_dt= [] 

def parse_content(text):
    doc=nlp(text)
    
    pattern7 = r'([A-Z]+\s+[A-Z]+)'
    name=re.findall(pattern7, text)[0]
    #print(re.findall(pattern7, text))
    print(name)
    
    pattern1=r'Tel.[8-9]+\d{9} '
    mobile=re.findall(pattern1,text)  
    mobile=mobile[0].replace('Tel','')
    print(mobile)
    
    email=[word for word in doc.like_email == True][0]
    print(email)
    
    pattern2=r'Registration No\D+\d+\D+\d+'
    vehicle_no=re.findall(pattern2,text)
    print(vehicle_no)
    
    pattern3=r'Policy No.[\d+\s]+'
    policy_no=re.findall(pattern3,text)
    policy_no=policy_no[0].replace('','')
    print(policy_no)
    
    pattern4=r"Period of InsuranceFrom\d+\D+\d+"
    period_from= re.findall(pattern4,text)
    period_from=(period_from)[0].replace('Period of InsuranceFrom','From')
    print(period_from)
    
    pattern5=r'To \d+\D+\d+'
    period_to= re.findall(pattern5,text)
    print(period_to)
    
    Name.append(name)
    Mobile_Number.append(mobile)
    Email_Id.append(email)
    Vehicle_no.append(vehicle_no)
    Policy_no.append(policy_no)
    Policy_start_dt.append(period_from)
    Policy_end_dt.append(period_to)
    
    print('Extraction completed  successfully')
    
#for f in file:


print('\n\nReading PDF File...')
text = extract_text(Path)
print(text)

#parse_content(text)