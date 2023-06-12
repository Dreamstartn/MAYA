
from Body.Speak import Speak
import urllib.request
#defines function and_ classes which help in opening urls
#url handling module for python
root_url = "http://192.168.195.227"

def sendRequest(url):
	n = urllib.request.urlopen(url) # send request to ESP

def LED_ON():
    sendRequest(root_url+"/ledon")
    Speak("switch is on")

def LED_OFF():
    sendRequest(root_url+"/ledoff")
    Speak("switch is off")


 