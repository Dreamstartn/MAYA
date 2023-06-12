import speech_recognition as sr
import pyfirmata




board = pyfirmata.Arduino('COM8')

it = pyfirmata.util.Iterator(board)
it.start()
board.digital[7].mode = pyfirmata.OUTPUT
board.digital[7].write(1)

def automate(query):
    
    if 'turn on' in query or 'open' in query:
        board.digital[7].write(0)
    elif "turn off" in query:
        board.digital[7].write(1)