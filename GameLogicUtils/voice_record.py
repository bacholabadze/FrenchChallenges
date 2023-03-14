import speech_recognition as sr

rec_vocale = sr.Recognizer()

# set the recording duration to 5 seconds
recording_duration = 5


def sound_recognition():
    transcripts = []
    with sr.Microphone() as source:
        print("Listening: ")
        try:
            audio = rec_vocale.listen(source)
        except sr.WaitTimeoutError:
            print("Recording timed out.")
        except KeyboardInterrupt:
            print("Recording stopped manually.")
    # transcribe the audio using Google Speech Recognition
    result = rec_vocale.recognize_google(audio, language='fr-FR')
    transcript = result['alternative'][0]['transcript']
    transcripts.append(transcript)
    print(result)
    print(transcripts)


while True:
    # use the default microphone as the audio source
    try:
        sound_recognition()
    except Exception as e:
        print(f"Try Again: Error code: {e}")
    else:
        print("Success")
        break

