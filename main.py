import pyttsx3
import PyPDF2

caminho = open('i-am-malala-1.pdf', 'rb') #local e nome do arquivo, no caso na mesma pasta
leitor = PyPDF2.PdfReader(caminho) #função de leitura do PDF
pagina = leitor.pages[0] #pega a primeira página

voz = pyttsx3.init('sapi5') #função de voz
voz.setProperty('rate', 150) #propriedades de voz
completo = ""

#loop para passar em todas as páginas, extrair o texto e adicionar ao arquivo
for pagina in leitor.pages: 
    texto = pagina.extract_text()
    completo = completo + texto
    voz.save_to_file(completo, "audiobook.mp3")
    voz.runAndWait()