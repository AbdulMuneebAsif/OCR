import pyttsx3

f2 = open("../TextFiles/TextToSpeech.txt", "a")


def textToSpeech(text):
    """ Method to convert Text To Speech """
    try:
        sound = pyttsx3.init()

        sound.say(text)
        sound.runAndWait()
        print(text)

        f2.write("\n\t\t\t=================================================================================== \n\n")
        f2.write(text)
        f2.write("\n\t\t\t=================================================================================== \n\n")
    except:
        print("Exception")


def textToSpeechWithoutPrint(text):
    """ Method to convert Text To Speech """
    try:
        sound = pyttsx3.init()

        sound.say(text)
        sound.runAndWait()

        f2.write("\n\t\t\t=================================================================================== \n\n")
        f2.write(text)
        f2.write("\n\t\t\t=================================================================================== \n\n")

    except:
        print("Exception")
