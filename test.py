import pyttsx3
import PyPDF2
import pdfplumber

arquivo = open('i-am-malala.pdf', 'rb')
leitor = PyPDF2.PdfReader(arquivo)
num_pagina = leitor.pages

voz = pyttsx3.init('sapi5')
voz.setProperty('rate', 150)
completo = ""

with pdfplumber.open(arquivo) as pdf:
    for i in range(num_pagina):
        pagina = pdf.pages[i]
        texto = pagina.extract_text()
        completo += texto
        voz.save_to_file(completo, "audiobook.mp3")
        voz.runAndWait()