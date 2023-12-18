from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
from abc import ABC, abstractmethod
import pandas as pd

# pip install fastpunct
# pip install textblob

project_id = 1071849374644
timeout_time = 1000
licznik_bledow = 0

class AudioToTextAbstract(ABC):
    @abstractmethod
    def get_text_from_audio(self, audio_path):
        pass

class GoogleSpeechToText(AudioToTextAbstract):    
    def __init__(self, audio_time, audio_path , language = "en-GB",model="long"):
        self.language = language
        self.model = model
        self.audio_time =  audio_time
        self.audio_path = audio_path

    #long video
    def get_text_from_audio(
        self,
        
        ) -> cloud_speech.BatchRecognizeResults:

        # Instantiates a client
        client = SpeechClient()
        config = cloud_speech.RecognitionConfig(
                auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
                language_codes=[self.language],
                model = self.model,
                
            )
      
        if(self.audio_time == "long"):
            

            file_metadata = cloud_speech.BatchRecognizeFileMetadata(uri=self.audio_path)

            request = cloud_speech.BatchRecognizeRequest(
                recognizer=f"projects/{project_id}/locations/global/recognizers/_",
                config=config,
                files=[file_metadata],
                recognition_output_config=cloud_speech.RecognitionOutputConfig(
                    inline_response_config=cloud_speech.InlineOutputConfig(),
                ),
            )

            # Transcribes the audio into text
            try:
                operation = client.batch_recognize(request=request)

                print("Waiting for operation to complete...")
                response = operation.result(timeout=timeout_time)
                text = ""
                for result in response.results[self.audio_path].transcript.results:
                    #print(f"Transcript: {result.alternatives[0].transcript}")
                    text = text + " " + str(result.alternatives[0].transcript)

             
                return text
                
            
            except ValueError: 
                return "Nie udało się zrozumieć mowy"
            
            except:
                licznik_bledow=licznik_bledow+1
                return "Błąd"
        
        
        elif(self.audio_time == "short"):
            
            with open(self.audio_path, "rb") as f:
                content = f.read()

            request = cloud_speech.RecognizeRequest(
                recognizer=f"projects/{project_id}/locations/global/recognizers/_",
                config=config,
                content=content,
            )
            
            # Transcribes the audio into text
            try:
                response = client.recognize(request=request)
                
                #for result in response.results:
                #   print(f"Transcript: {result.alternatives[0].transcript}")
                text = ""
                for result in response.results:
                    text  = text + " " + result.alternatives[0].transcript
            
                
                return text
            
            except ValueError:
                return "Nie udało się zrozumieć mowy"
            
            except:
                licznik_bledow=licznik_bledow+1
                return "Błąd"

        
        else:
            return "Bad audio_time argument"
            

start=0
stop=1000

data_file = "F:/cv-corpus-15.0-2023-09-08-pl/cv-corpus-15.0-2023-09-08/pl/validated.tsv"
sound_files = "F:/cv-corpus-15.0-2023-09-08-pl/cv-corpus-15.0-2023-09-08/pl/clipswav/"
transcryption_path = "google_transcryption/with_punctuation/"
pd1 = pd.read_csv(data_file,sep="\t",header=0)
#tranksrypcja()
#print(pd1['path'])

for i in range(start,2):
    if(licznik_bledow>15):
        break
    f = open(transcryption_path+ pd1['path'][i].split(".")[0]+"_transcryption"+".txt",mode='w',encoding = "utf-8")
    #objekt = GoogleSpeechToText("short",sound_files+pd1['path'][i],language="pl_PL") #mp3
    print(pd1['path'][i].split(".")[0]+".wav")
    objekt = GoogleSpeechToText("short",sound_files+pd1['path'][i].split(".")[0]+".wav",language="pl_PL") #wav
  
    f.write(objekt.get_text_from_audio())
    f.close()
    
    #print(transkrypcja(model_list[model_number],sound_files + pd1['path'][0])['text'])
