
import argparse
import io

from google.cloud import speech_v1p1beta1

import grpc

def transcribe_onprem(
    local_file_path: str,
    api_endpoint: str,
) -> speech_v1p1beta1.RecognizeResponse:
    """
    Transcribe a short audio file using synchronous speech recognition on-prem

    Args:
      local_file_path: The path to local audio file, e.g. /path/audio.wav
      api_endpoint: Endpoint to call for speech recognition, e.g. 0.0.0.0:10000

    Returns:
      The speech recognition response
          {
    """
    # api_endpoint = '0.0.0.0:10000'
    # local_file_path = '../resources/two_channel_16k.raw'

    # Create a gRPC channel to your server
    channel = grpc.insecure_channel(target=api_endpoint)
    transport = speech_v1p1beta1.services.speech.transports.SpeechGrpcTransport(
        channel=channel
    )

    client = speech_v1p1beta1.SpeechClient(transport=transport)

    # The language of the supplied audio
    language_code = "en-US"

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 16000

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = speech_v1p1beta1.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "encoding": encoding,
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(request={"config": config, "audio": audio})
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        print(f"Transcript: {alternative.transcript}")

    return response

tekst = transcribe_onprem('OSR_us_000_0010_8k.wav','0.0.0.0:10000')