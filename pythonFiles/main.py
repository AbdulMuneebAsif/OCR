import mijRIT
import mijTTS
import mijSteg


def menu():
    while True:

        print("\n\t\t\t ============================ MENU ================================\n")

        print("0. stop / terminate / end")
        print("1. Convert Image to Text")
        print("2. Convert Text to Speech")
        print("3. Steganography --> hide data into image")

        print("\n\t\t\t ==================================================================\n")
        choice = int(input("Enter You Choice : "))

        if choice == 0:
            exit()
        elif choice == 1:
            mijRIT.mainMenu()
        elif choice == 2:
            text = input("Enter Your Text here => ")
            mijTTS.textToSpeech(text)
        elif choice == 3:
            mijSteg.stegnography()


if __name__ == '__main__':
    menu()
