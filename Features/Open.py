import os
import keyboard
import pyautogui
import webbrowser
from keyboard import press_and_release
from time import sleep
from Body.Speak import Speak

def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        Nameofweb=Nameofweb.replace(" ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        Nameofweb = Query.replace("launch ","")
        Nameofweb=Nameofweb.replace(" ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "open" in Query:
        Nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)  
        return True
        
    elif "folder" in Query:
        Nameoffolder = Query.replace("search ","").replace("folder",""),
        pyautogui.press('win')
        sleep(1)
        keyboard.write(f"folder:{Nameoffolder}")
        sleep(4)
        keyboard.press('enter')
        sleep(1)  
        return True
        
    elif "document" in Query:
        Nameofdocument = Query.replace("search","").replace("document","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(f"document:{Nameofdocument}")
        sleep(4)
        keyboard.press('enter')
        sleep(1)  
        return True     
        
    

    elif "start" in Query:
        Nameoftheapp = Query.replace("start ","")

        if "chrome" in Nameoftheapp:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return True

def CloseExe(Query):
   Query = str(Query).lower()
   
   
   if 'excel' in Query:
         os.system("TASKKILL /F /IM EXCEL.EXE")        
      
   elif 'word' in Query: 
         os.system("TASKKILL /F /IM WINWORD.exe")
      
   elif 'spotify' in Query: 
         os.system("TASKKILL /F /IM spotify.exe")
      
   elif 'chrome' in Query: 
         os.system("TASKKILL /F /IM chrome.exe")
      
   elif 'powerpoint' in Query: 
         os.system("TASKKILL /F /IM POWERPNT.exe")   
   
   elif "window" in Query:
         press_and_release("Alt+F4") 