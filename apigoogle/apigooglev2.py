from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

#long video
def transcribe_batch_gcs_input_inline_output_v2(
    project_id: str,
    gcs_uri: str,
    language = "en-GB",
    model="latest_long"
) -> cloud_speech.BatchRecognizeResults:
    """Transcribes audio from a Google Cloud Storage URI.

    Args:
        project_id: The Google Cloud project ID.
        gcs_uri: The Google Cloud Storage URI.

    Returns:
        The RecognizeResponse.
    """
    # Instantiates a client
    client = SpeechClient()

    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
        #language_codes=["en-GB"],
        language_codes=[language],
        #model="long",
        #features=cloud_speech.RecognitionFeatures(
        #    enable_automatic_punctuation=True,
        #),
        model = "long",
    )

    file_metadata = cloud_speech.BatchRecognizeFileMetadata(uri=gcs_uri)

    request = cloud_speech.BatchRecognizeRequest(
        recognizer=f"projects/{project_id}/locations/global/recognizers/_",
        config=config,
        files=[file_metadata],
        recognition_output_config=cloud_speech.RecognitionOutputConfig(
            inline_response_config=cloud_speech.InlineOutputConfig(),
        ),
    )

    # Transcribes the audio into text
    operation = client.batch_recognize(request=request)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=1200)

    for result in response.results[gcs_uri].transcript.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

    return response.results[gcs_uri].transcript

# short video
def transcribe_file_v2(
    project_id: str,
    audio_file: str,
) -> cloud_speech.RecognizeResponse:
    # Instantiates a client
    client = SpeechClient()

    # Reads a file as bytes
    with open(audio_file, "rb") as f:
        content = f.read()

    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
        language_codes=["en-US"],
        model="latest_long",
    )

    request = cloud_speech.RecognizeRequest(
        recognizer=f"projects/{project_id}/locations/global/recognizers/_",
        config=config,
        content=content,
    )

    # Transcribes the audio into text
    response = client.recognize(request=request)

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

    return response

# pierwszy argument to identyfikator kontenera, nie zmieniajcie, drugi to miejsce przechowywania w kontenerze pliku, zmieniajcie tylko nazwe pliku
# np. gs://speechapi_storage/plik1.flac, gs://speechapi_storage/plik2.flac, 3 to język nagrania, domyślnie angielski
#tekst = transcribe_batch_gcs_input_inline_output_v2("1071849374644","gs://speechapi_storage/OSR_us_000_0010_8k.wav",)

# pierwszy argument to identyfikator kontenera, nie zmieniajcie, drugi to ścieżka do pliku lokalnego
tekst = transcribe_file_v2("1071849374644","test3.wav")