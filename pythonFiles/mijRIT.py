import pytesseract
from PIL import Image

path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
f = open("../TextFiles/ExtractedText.txt", "a")


def extractText(filename):
    """This Function Extract the Text From an Image"""
    try:
        pytesseract.pytesseract.tesseract_cmd = path
        img = Image.open(filename)

        text = pytesseract.image_to_string(img)
        return text
    except:
        print("exception....\n")


def writeText(filename):
    """This Function Will Write The Extracted Text of Image"""
    try:
        text = extractText(filename)
        f.write(text)
        f.write("\n\t\t\t =================================================================================== \n\n")
    except:
        print("exception....\n")


def printText(filename):
    """This Function Will Print Extracted Text of Image"""
    text = extractText(filename)
    print(text)


def result(filename):
    """This Function Will Print And Write The Extracted Text of Image"""
    writeText(filename)
    printText(filename)


def title():
    """ This Function Will Print the Title """

    print("\n\n")
    print("\t\t\t\t =============================================================================================== ")
    print("\t\t\t\t ============================ READ IMAGE TEXT AND WRITE IN NEW FILE ============================ ")
    print("\t\t\t\t =============================================================================================== ")
    print("\n\n")


def mainMenu():
    """ This Function is for Menu """
    title()
    while 1:

        print('===========================================\n')
        print("Press 0 to stop / exit terminate ")
        print("Press 1 to continue \n")
        print('===========================================\n')

        terminate = eval(input("Enter Your Choice          : "))

        if terminate == 0:
            exit()
        elif terminate == 1:
            filename = input("Enter File Path and Name   : ")
            print("\n =================================================\n")
            result(filename)
        else:
            print("Invalid Input....\n")
