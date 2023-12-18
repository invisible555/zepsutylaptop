
from email import header
from pyannote.audio import Pipeline
import pandas as pd

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token="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")

audio_path = "jadamian"
# send pipeline to GPU (when available)
import torch
pipeline.to(torch.device("cuda"))

# apply pretrained pipeline
diarization = pipeline(audio_path + ".wav")
lista = []
# print the result
for turn, _, speaker in diarization.itertracks(yield_label=True):
    #print(f"start={turn.start:.1f}s stop={turn.end:.1f}s speaker_{speaker}")
    lista.append(str(turn.start) + " " + str(turn.end) + " " + str(speaker))
# start=0.2s stop=1.5s speaker_0
# start=1.8s stop=3.9s speaker_1
# start=4.2s stop=5.7s speaker_0

for i in lista:
    print(i)


'''
f = open(audio_path+"speakers"+".txt",mode='w',encoding = "utf-8")
for i in lista:
    f.write(i + '\n')
f.close()
'''
