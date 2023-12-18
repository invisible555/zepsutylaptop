
import argparse
from ssl import CHANNEL_BINDING_TYPES

from google.cloud import speech


def transcribe_file_with_enhanced_model(path: str) -> speech.RecognizeResponse:
    """Transcribe the given audio file using an enhanced model."""

    client = speech.SpeechClient()

    # path = 'resources/commercial_mono.wav'
    with open(path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        language_code="en-US",
        use_enhanced=True,
        # A model must be specified to use enhanced model.
        audio_channel_count=2,
        model="telephony",
    )

    response = client.recognize(config=config, audio=audio)

    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print(f"First alternative of result {i}")
        print(f"Transcript: {alternative.transcript}")

    return response

tekst = transcribe_file_with_enhanced_model("C:/Users/niewi/Desktop/Audio-Denoising-master/nagrania/test3.wav")
#print(tekst)
