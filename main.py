import pyttsx3
import PyPDF2

caminho = open('i-am-malala.pdf', 'rb')
leitor = PyPDF2.PdfReader(caminho)
pagina = leitor.pages[0]

voz = pyttsx3.init('sapi5')
voz.setProperty('rate', 150)
completo = "Audiobook"

for pagina in leitor.pages:
    texto = pagina.extract_text()
    completo = completo + texto
    voz.save_to_file(completo, "audiobook.mp3")
    voz.runAndWait()