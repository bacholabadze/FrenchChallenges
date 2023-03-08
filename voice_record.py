import speech_recognition as sr

rec_vocale = sr.Recognizer()

# set the recording duration to 5 seconds
recording_duration = 3

# use the default microphone as the audio source
with sr.Microphone() as source:
    print("Listening: ")
    try:
        audio = rec_vocale.listen(source, timeout=recording_duration)
    except sr.WaitTimeoutError:
        print("Recording timed out.")
    except KeyboardInterrupt:
        print("Recording stopped manually.")
# transcribe the audio using Google Speech Recognition
result = rec_vocale.recognize_google(audio, language='fr-FR')

print(result)
