from tkinter import filedialog
import pytesseract as tess
from PIL import Image
import main
import mijTTS

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

f = open("../TextFiles/MultipleImagesTextExtracted.txt", "a")


def extract():
    files = filedialog.askopenfilenames(title="Select Images")

    text = []

    n = len(files)

    for i in range(0, n):
        f.write("\n\t\t\t===========================================================================\n\n")
        print("\n\t\t\t =========================================================================== \n\n")
        img = Image.open(files[i])
        text.append(tess.image_to_string(img))
        print(text[i])
        f.write(text[i])

        optionToPlaySound = input("Do you want to convert this text into speech (yes/no) : ")
        tts = optionToPlaySound
        tts.lower()

        if tts == 'yes':
            mijTTS.textToSpeechWithoutPrint(text[i])
        elif tts == 'no':
            print()
        else:
            print("invalid Input....")

        searchWordOccurrence = input("Do you want to find the occurrence of any word (yes/no) : ")

        if searchWordOccurrence == "yes" or searchWordOccurrence == "Yes" or searchWordOccurrence == "YES":
            # The string to search in
            string = text[i]

            # The word to search for
            word = input("Enter any to find its occurrence => ")

            # Convert the string and the word to lowercase
            string = string.lower()
            word = word.lower()

            # Count the occurrences of the word in the string
            count = string.count(word)

            # Print the result
            print("The word '" + word + "' appears " + str(count) + " times in the text.")
        elif searchWordOccurrence == "no" or searchWordOccurrence == "No" or searchWordOccurrence == "NO":
            print()
        else:
            print("invalid Input....")


if __name__ == '__main__':
    extract()
    main.menu()
