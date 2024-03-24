import speech_recognition as sr
import pyttsx3

audio = sr.Recognizer()
maquina = pyttsx3.init()
maquina.say('Hello, my name is nala')
maquina.runAndWait()

try:
    with sr.Microphone() as source:
        print('ouvindo..')
        voz = audio.listen(source)
        comando = audio.recognize_google_cloud(voz, language='pt-br')
        comando = comando.lower()
        if 'nala' in comando:
            print(comando)

except:
    print('deu ruim')
