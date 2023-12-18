from os import path
from pydub import AudioSegment
import pandas as pd

data_file = "F:/cv-corpus-15.0-2023-09-08-pl/cv-corpus-15.0-2023-09-08/pl/validated.tsv"
sound_files = "F:/cv-corpus-15.0-2023-09-08-pl/cv-corpus-15.0-2023-09-08/pl/clips/"
data_export = "F:/cv-corpus-15.0-2023-09-08-pl/cv-corpus-15.0-2023-09-08/pl/clipswav/"
pd1 = pd.read_csv(data_file,sep="\t",header=0)
#start=0
#stop=96209
start = 96209
stop = pd1['path'].count()
for i in range(start,stop,1):
    sound = AudioSegment.from_mp3(sound_files+pd1['path'][i])
    sound.export(data_export+pd1['path'][i].split(".")[0]+".wav", format="wav")
# files                                                                         
#src = "transcript.mp3"
#dst = "test.wav"

# convert wav to mp3                                                            
#sound = AudioSegment.from_mp3(src)
#sound.export(dst, format="wav")