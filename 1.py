import socket
import time
listensocket = socket.socket()
port = 8000
maxconnections = 999
IP = socket.gethostname()
listensocket.bind(('',port))
listensocket.listen(maxconnections)
print("Server started on ",IP," on port ",port)
(clientsocket,address) = listensocket.accept()
print("connection made! ")
running = True

import pyttsx3
voiceEngine = pyttsx3.init()

from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("siren.wav")
 
newVoiceRate = 130
voiceEngine.setProperty('rate', newVoiceRate)
voiceEngine.setProperty('volume',0.8)

while running:
  message = clientsocket.recv(1024).decode()
  if message!="":
    if(message=="Unknown"):
      play(song)
