import speech_recognition as sr

AUDIO_FILE="Week 5/de cock ravi.wav"

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

# read the audio file 

try:
    print("Audio file contain : " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError:
    print("Could not get result from google speech recognition")