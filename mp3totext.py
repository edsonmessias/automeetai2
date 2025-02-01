
import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "da8a481c8fea4c5aa5e62c7df6bef8ce"

# URL of the file to transcribe
FILE_URL = "C:/Users/Administrator/PycharmProjects/automeetai2/2674dededaec4c75af4f18b881906fe3.mp3"

# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.best,
                                 language_code='pt',
                                 speaker_labels=True,
                                 speakers_expected=2)
#language_detection=True
transcriber = aai.Transcriber(config=config)
transcript = transcriber.transcribe(FILE_URL)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    for utt in transcript.utterances:
        print(f"{utt.speaker}: {utt.text}")
        print('\n')
