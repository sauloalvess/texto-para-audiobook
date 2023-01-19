import pyttsx3
import PyPDF2

ler_arquivo = open("C:\Users\saulo\Downloads\i-am-malala.pdf", "rb")
livro = PyPDF2.PdfFileReader(ler_arquivo)
paginas = livro.numPages

voz = pyttsx3.init('sapi5')
voz.setProperty('rate', 150)

#pagina = livro.getPage(0)

for i in range(0, paginas):
    texto = paginas[i]
    voz.save_to_file(texto, "audiobook.mp3")