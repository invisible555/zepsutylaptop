import pandas as pd
import re
import string

import inflect

p = inflect.engine()
print(p.number_to_words(100))
'''

def remove_punctuation(text):
    #return text.translate(str.maketrans("", "", string.punctuation))
    return text.translate(str.maketrans("", "", string.punctuation))

def remove_punctuation2(text):
     return re.sub(r'[^a-zA-Z0-9ąćęłńóśźż\s]', '', text)
    #return test_str

def compare_strings_without_spaces(str1, str2):
    # Remove white spaces from both strings
    str1_no_spaces = ''.join(str1.split())
    str2_no_spaces = ''.join(str2.split())

    # Compare the modified strings
    return str1_no_spaces == str2_no_spaces

start=0
stop=1000
correct=0
incorrect=0
errors=0

audio_path = "google_transcryption/mp3/"
data_file = "F:/cv-corpus-15.0-2023-09-08-pl/cv-corpus-15.0-2023-09-08/pl/validated.tsv"
pd1 = pd.read_csv(data_file,sep="\t",header=0)  
pd1 = pd1.replace(',', '', regex=True)
#pd1['sentence'] = pd1['sentence'].apply(lambda x: remove_punctuation2(x.lower()))
#pd1['sentence'] = pd1['sentence'].apply(lambda x: x.replace("  "," "))
for i in range(start,stop,1):
    try:
        f = open(audio_path+pd1['path'][i].split(".")[0]+"_transcryption"+".txt",mode='r',encoding = "utf-8")
        cos=f.read()
        
        if(len(cos) == 0 ):
            print(pd1['path'][i])
            errors=errors+1
            continue
        if(cos[0]==" " or cos[0]=="-"):
            cos=cos[1:]

        #if(compare_strings_without_spaces(remove_punctuation(pd1['sentence'][i].lower()), cos.lower())):
        if(cos.lower()==pd1['sentence'][i].lower()):
            correct=correct+1
        else:
            incorrect=incorrect+1
            #print(pd1['sentence'][i].lower())
            #print(cos.lower())
    except:
        print(pd1['path'][i])
        errors=errors+1
        continue

print(correct)
print(incorrect)
print(errors)
'''