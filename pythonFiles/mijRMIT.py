from tkinter import filedialog
import pytesseract as tess
from PIL import Image

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract():
    files = filedialog.askopenfilenames(title="Select Images")

    text = []

    n = len(files)

    for i in range(0, n):
        print("\n\n =========================================================================== \n\n")
        img = Image.open(files[i])
        text.append(tess.image_to_string(img))
        print(text[i])


if __name__ == '__main__':
    extract()
