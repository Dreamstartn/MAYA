
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import os
import pyautogui
import keyboard 
from time import sleep
from selenium import webdriver
import pandas as pd
from Body.Speak import Speak
import pathlib
from Body.Listen import MicExecution
from selenium.webdriver.support import expected_conditions as EC

scriptDirectory = pathlib.Path().absolute()

options = Options()

options.add_argument("--profile-directory=Default")
options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
PathofDriver = "DataBase\\chromedriver"
driver = webdriver.Chrome(PathofDriver,options=options)
#driver.maximize_window()
driver.get("https://web.whatsapp.com/")

 
ListWeb = {'nitesh' : "+91908XXXXXXXX",
           }
          

def WhatsappSender(Name):
    Speak(f"Preparing To Send a Message To {Name}")
    Speak("What's The Message By The Way?")
    Message = MicExecution()
    Number = ListWeb[Name]
    LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
    driver.get(LinkWeb)
    sleep(5)
    try:
        send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span")))
        send_button.click()
        Speak("Message Sent")
    except:
       print("Invalid Number")

   
     

