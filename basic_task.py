
import datetime
from Body.Speak import Speak
import wikipedia
import webbrowser
import os
import subprocess
from keyboard import press_and_release
import time
from pyautogui import click
import requests
import pywhatkit
import wikipedia as googleScrap
from Body.Listen import Listen





def Time():
 time=datetime.datetime.now().strftime("%H:%M")
 Speak(time) 

def Date():
 date=datetime.date.today()
 Speak(date)
 
def Day():
 day=datetime.datetime.now().strftime("%A")
 Speak(day) 
 

def NonInput_func(query):
 query=str(query)
 
 
 
 if "shutdown" in query:
       Speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
       subprocess.call(["shutdown", "/p"])
        
 
 elif "restart" in query :
       Speak("Ok , your pc will restart in 10 sec make sure you exit from all applications")           
       subprocess.call(["shutdown", "/r"])
   

 
 elif "take screenshot" in query:
   press_and_release("Win+shift+s")
   
def auto(query):
  if "new tab" in query:
             press_and_release('ctrl+t')
             
  elif "new window" in query:
             press_and_release('ctrl+n')
              
  elif "close tab" in query:
             press_and_release('ctrl+w')
         
  elif "open history" in query:
             press_and_release('ctrl+h') 

  elif "reload" in query:
             press_and_release('ctrl+r')
           
  elif "add to bookmark" in query:
             press_and_release('ctrl+d')  
             
  elif "open download folder" in query:
             press_and_release('ctrl+j')
             
def Basic_commands(query):
  if "copy" in query:
    press_and_release('ctrl+c')
  
  elif "cut" in query:
    press_and_release('ctrl+x') 
   
  elif "paste" in query:
    press_and_release('ctrl+p')   
    
    
def Input_func(query):
  
  
      
  if "google search" in query:
    query = query.lower()
    query = query.replace("Maya","")
    query = query.replace("google","")
    query = query.replace("search","")
    query = query.replace("on","")
    query = query.replace("can you search on google","")
    
    Speak("What you want to search")
    ques =Listen()
    Speak("Ok, This Is The Result For Your Search Sir.")
    pywhatkit.search(ques)
    click(x=1181, y=19)
    try:
        result = googleScrap.summary(ques,2)
        Speak(result)
        os.system("TASKKILL /F /im chrome.exe")
    except:
        Speak("Sorry, No Speakable Query Available Sir") 
        return True
        
  elif 'youtube search' in query:
  
      Speak("What you want to search on youtube")
      ques=Listen()
    
      web ='https://www.youtube.com/results?search_query=' + ques
      webbrowser.open(web) 
      Speak('this is what i found')