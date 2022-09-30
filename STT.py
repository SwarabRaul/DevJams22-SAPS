import speech_recognition as spr

# obtain audio from the microphone
r = spr.Recognizer()
with spr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except spr.UnknownValueError:
    print("Sphinx could not understand audio")
except spr.RequestError as e:
    print("Sphinx error; {0}".format(e))