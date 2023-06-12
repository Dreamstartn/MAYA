import subprocess
from Body.Listen import Listen
from Body.Speak import Speak


def TV(command):
 
  if command=="on tv":
 # send power button event to turn on the Android TV
     subprocess.call(['adb', 'shell', 'input', 'keyevent', '26'])
  elif command=="off tv":
     subprocess.call(['adb', 'shell', 'input', 'keyevent', '26'])
   
  elif command=="volume up": 
     subprocess.call(['adb', 'shell', 'input', 'keyevent', '24'])

  elif command=="volume down": 
      subprocess.call(['adb', 'shell', 'input', 'keyevent', '25'])

  elif command=="volume down": 
      subprocess.call(['adb', 'shell', 'input', 'keyevent', '25'])  
  
  elif command=="open youtube": 
    Speak("What you want to search on youtube")
    query=str(Listen())
    subprocess.call(['adb', 'shell', 'am', 'start', '-n', 'com.google.android.youtube.tv/com.google.android.apps.youtube.tv.activity.ShellActivity'])

    subprocess.call(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_DPAD_UP'])
  
    subprocess.call(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_DPAD_UP'])

    # Type the search query
    subprocess.call(['adb', 'shell', 'input', 'text', query])

    # Press the Enter key to start the search
    subprocess.call(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_ENTER'])   
