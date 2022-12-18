import pyttsx3


def textToSpeech(text):
    """ Method to convert Text To Speech """
    try:
        sound = pyttsx3.init()

        sound.say(text)
        sound.runAndWait()

    except:
        print("Exception")

