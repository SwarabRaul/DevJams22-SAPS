import speech_recognition as spr

def main():
    r = spr.Recognizer()

    with spr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please Speak: ")
        audio = r.listen(source)

        try:
            print("You Said: " + r.recognize_google(audio))
        except spr.RequestError as e:
            print("Error: " + str(e))

if __name__ == "__main__":
    while(1):
        main()