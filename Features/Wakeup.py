import speech_recognition as sr

def Listen_W():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # Listening Mode.....
    
    try:
        print("")
        query = r.recognize_google(audio,language="en-in")

    except:
        return ""
    
    query = str(query).lower()
    print(query)
    return query

def WakeupDetected():

    while True:

        queery = Listen_W().lower()

        if "wake up" in queery:
            return "True-Mic"
        
        else:
            pass