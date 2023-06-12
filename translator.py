import speech_recognition as sr

from googletrans import LANGUAGES, Translator
from Body.Speak import Speak
from Body.Listen import Listen

def translator1():

 def listen_1():
        translator = Translator()
        
    # Initialize the recognizer
        r = sr.Recognizer()

        # Use the microphone as source
        with sr.Microphone() as source:
            Speak("tell me the word or sentences you want to translate")
            print("Speak now...")
            audio = r.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            text = r.recognize_google(audio, language=source_lang)

            # Translate the text to the destination language
            translation = translator.translate(text, src=source_lang, dest=dest_lang)

            # Print the translation
            print(f"Translation: {translation.text}")

            Speak(translation.text)
        
        

        except sr.UnknownValueError:
            print("Could not understand audio")

   
 # Take input from user for source language
 while True:
    Speak("Enter the source language")
    source_lang_name = Listen()
    if source_lang_name.lower() in LANGUAGES.values():
        source_lang = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(source_lang_name.lower())]
        break
    else:
        print("Invalid source language, please try again.")

 while True:
    Speak("Enter the destination language")
    dest_lang_name =Listen()
    if dest_lang_name.lower() in LANGUAGES.values():
        dest_lang = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(dest_lang_name.lower())]
        break
    else:
        print("Invalid destination language, please try again.")

 listen_1()

 Speak("You want to translate something else")
 response=Listen()
 if response=="yes":
    translator1()
 else:
   Speak("I am glad to serve you")  


