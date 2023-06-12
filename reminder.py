import winsound
from win10toast import ToastNotifier
from Body.Listen import Listen
from Body.Speak import Speak

def timer (remider,seconds):
    notificator=ToastNotifier()
    notificator.show_toast("Reminder",f"""Alarm will go off in {seconds} Seconds.""",duration=20)
    notificator.show_toast(f"Reminder",remider,duration=20)

    #alarm
    frequency=2500
    duration=20000
    winsound.Beep(frequency,duration)

def reminder():
    Speak("What would you remindes of:")
    print("What would you remindes of:")
    words=Listen()
    print(words)
    sec=int(input("Enter seconds: "))
    timer(words,sec)

reminder()    