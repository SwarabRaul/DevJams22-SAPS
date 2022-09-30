import speech_recognition as spr

r = spr.Recognizer()
r.adjust_for_ambient_noise(source2, duration=0.2)
with spr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except spr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except spr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))