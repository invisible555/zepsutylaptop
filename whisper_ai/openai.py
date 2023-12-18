
import whisper

audio_path = "nagranieinternet"
model = whisper.load_model("medium")
result = model.transcribe("F:/cv-corpus-15.0-2023-09-08-pl/cv-corpus-15.0-2023-09-08/pl/clips/"+"common_voice_pl_20547774.mp3")
print(result)
'''
f = open(audio_path+"transcryption"+".txt",mode='w',encoding = "utf-8")
for i in range(0,29,1):
    print(str(result["segments"][i]["start"]) + "   " + str(result["segments"][i]["end"]) + "   " + str(result["segments"][i]["text"]))
    f.write(str(result["segments"][i]["start"]) + "   " + str(result["segments"][i]["end"]) + "   " + str(result["segments"][i]["text"]) + '\n')
f.close()
'''
'''
model = whisper.load_model("medium")

# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio('jadamian.wav')

audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# print the recognized text
print(result.text)

'''