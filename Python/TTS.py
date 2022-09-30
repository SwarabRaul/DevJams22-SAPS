import pyttsx3

engine = pyttsx3.init()

# Rates
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 125)

# Voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

while(1):
    text = str(input("Please Enter a Text: "))
    engine.say(text)
    engine.runAndWait()