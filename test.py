import pyttsx3
import PyPDF3

caminho = open('i-am-malala-1.pdf', 'rb')
leitor = PyPDF3.PdfFileReader(caminho)
pagina = leitor.numPages

voz = pyttsx3.init('sapi5')
voz.setProperty('rate', 150)
completo = "Audiobook"

for pagina in leitor.pages:
    texto = pagina.extractText()
    completo = completo + texto
    voz.save_to_file(completo, "audiobookpypdf3.mp3")
    voz.runAndWait()