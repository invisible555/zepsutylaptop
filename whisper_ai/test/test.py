import numpy as np
import pandas as pd
import whisper

#start=0
#stop=1000
start=0
stop=1000
model_number=4
def transkrypcja(model,audio_path):
    model = whisper.load_model(model)
    result = model.transcribe(audio_path)
    return result


model_list = ["tiny","base","small","medium","large"]
data_file = "F:/cv-corpus-15.0-2023-09-08-pl/cv-corpus-15.0-2023-09-08/pl/validated.tsv"
sound_files = "F:/cv-corpus-15.0-2023-09-08-pl/cv-corpus-15.0-2023-09-08/pl/clips/"
transcryption_path = "mp3_transcryption/"
pd1 = pd.read_csv(data_file,sep="\t",header=0)
#tranksrypcja()
#print(pd1['path'])

for j in range(model_number,len(model_list)):
    for i in range(start,stop):
        print(i)
        #print(model_list[model_number])
        print(transcryption_path+model_list[model_number]+"/"+ pd1['path'][i].split(".")[0]+"_transcryption"+".txt")
        f = open(transcryption_path+model_list[model_number]+"/"+ pd1['path'][i].split(".")[0]+"_transcryption"+".txt",mode='w',encoding = "utf-8")
        f.write(transkrypcja(model_list[model_number],sound_files + pd1['path'][i])['text'])
        f.close()
        #print(transkrypcja(model_list[model_number],sound_files + pd1['path'][0])['text'])
    model_number=model_number+1
    


