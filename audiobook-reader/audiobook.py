# AUDIOBOOK READER

# Program that reads pdf file turning it into an audiobook

# Relax and listen

import pyttsx3
import PyPDF2

book = open('oop_python.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
startPage = 7
for num in range(startPage, pages):
    page = pdfReader.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
