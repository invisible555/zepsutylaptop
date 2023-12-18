import pandas as pd
import re
import string

import Levenshtein

def calculate_similarity_ratio(str1, str2):
    distance = Levenshtein.distance(str1, str2)
    max_len = max(len(str1), len(str2))
    return 1 - distance / max_len

def calculate_edit_distance(str1, str2):
    return Levenshtein.distance(str1, str2)

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
licznik=0
lista_Levenshtein=[]
licznik_Levenshtein=[]

audio_path = "whisperai_transcryption/mp3/large/"
data_file = "F:/cv-corpus-15.0-2023-09-08-pl/cv-corpus-15.0-2023-09-08/pl/validated.tsv"
pd1 = pd.read_csv(data_file,sep="\t",header=0)
pd1 = pd1.replace(',', '', regex=True)
pd1['sentence'] = pd1['sentence'].apply(lambda x: remove_punctuation2(x.lower()))
pd1['sentence'] = pd1['sentence'].apply(lambda x: x.replace("  "," "))
pd1['sentence'] = pd1['sentence'].apply(lambda x: x.replace("-"," "))
for i in range(start,stop,1):
    try:
        f = open(audio_path+pd1['path'][i].split(".")[0]+"_transcryption"+".txt",mode='r',encoding = "utf-8")
        cos=f.read()
        if(len(cos) == 0 ):
            errors=errors+1
            continue

        if(cos[0]==" " or cos[0]=="  " or cos[0]=="-"):
            cos=cos[1:]
        cos=remove_punctuation(cos)
        #if(compare_strings_without_spaces(remove_punctuation(pd1['sentence'][i].lower()), cos.lower())):
        if(compare_strings_without_spaces(cos.lower(),pd1['sentence'][i].lower())):
            correct=correct+1
        else:          
            
            similarity_ratio = calculate_similarity_ratio(pd1['sentence'][i].lower(), cos.lower())
            if(similarity_ratio > 0.0):
                licznik=licznik+1
                distance = calculate_edit_distance(pd1['sentence'][i].lower(), cos.lower())
                if(distance not in lista_Levenshtein):
                    lista_Levenshtein.append(distance)
                    licznik_Levenshtein.append(1)
                else:
                    index = lista_Levenshtein.index(distance)
                    licznik_Levenshtein[index] += 1
                #print(f"Edit distance between '{pd1['sentence'][i].lower()}' and '{cos.lower()}': {distance}")
                #print(f"Similarity ratio between '{pd1['sentence'][i].lower()}' and '{cos.lower()}': {similarity_ratio}")

            incorrect=incorrect+1
            print(pd1['sentence'][i].lower())
            print(cos.lower())
    except:

        errors=errors+1
        continue

print(correct)
print(incorrect)
print(errors)
'''
for i in range(len(lista_Levenshtein)):
    print("odległość levenstein: " +str(lista_Levenshtein[i]) + " liczba wystapien: " + str(licznik_Levenshtein[i]))
print(licznik)
'''