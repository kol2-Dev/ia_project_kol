# PÁGINA DE TESTES PARA O NALA-IA

import speech_recognition as sr


#r é o reconhecedor..se eu quiser, posso atribuir outro nome
r = sr.Recognizer()

#abrir o mic

with sr.Microphone() as source:
    audio = r.listen(source)

    print(r.recognize_google(audio))
    
