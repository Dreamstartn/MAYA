
from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
from Main import MainTaskExecution
from Body.Speak import Speak
from Features.Clap import Tester
from Features.Wakeup import WakeupDetected


print(">> Starting The Maya : Wait For Some Seconds.")
print(">> Started The Maya : Wait For Few Seconds More")





def MainExecution():
    Speak("Hello Sir")
    Speak("I'm Maya, I'm Ready To Assist You Sir.")

    while True:

        Data = MicExecution()
        Data = str(Data).replace(".","")

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass

        elif len(Data)<3:
            pass

        elif "send message" in Data:
          pass
          
        elif "send email"  in Data:
         pass
        
        elif "time" in Data:
         pass
         
        elif "day" in Data:
         pass
        
        elif "date" in Data:
         pass
         
        elif "new tab" in Data:
         pass
          
        elif "search on youtube" in Data or "can you search on youtube" in Data:
         pass
         
        elif "search on google" in Data or "can you search on google" in Data:
         pass 
         
        elif "new window" in Data:
         pass
         
        elif "history" in Data:
         pass
         
        elif "shutdown" in Data:
         pass
         
        elif "restart" in Data:
         pass 
         
        elif "bookmark this page" in Data or "create a bookmark"  in Data or "bookmark" in Data:
         pass
         
        elif "turn on" in Data:
         pass
         
        elif "turn off" in Data:
         pass

        elif "on translator" in Data or "on the translator" in Data or "i need to translate something" in Data or "turn on translator" in Data :
         pass   
         
        elif "turn on the tv" in Data or "turn on tv" in Data or "switch on tv" in Data or "on tv" in Data or "please turn on tv" in Data:
          pass

        elif  "take some rest" in Data or "stop" in Data:
           Speak("ohk sir, any time you call me i am available in your service")
           Wakeup() 
           break 

        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)

        else:
           
            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
       print("")
       MainExecution()
       
    else:
      pass 
def Wakeup():
   query=WakeupDetected()    
   if "True-Mic" in query:
     print()
     MainExecution()
   
   else:
     pass
    


#ClapDetect()
#Wakeup() 
MainExecution()

