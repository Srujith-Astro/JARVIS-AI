import speech_recognition as sr
import os
import webbrowser
import datetime

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language= "en-in")
            print (f"User said : {query}")
            return query
        except Exception() as e:
            return "Some error Occured. Sorry from jarvis"
        
if __name__ == '__main__':
    print('Spyder')
    say ("Hello I am Jarvis AI")
    while True:
        
        print("Listening")
        query = takeCommand()
        sites = [["Youtube , "https://www.youtube.com"], ["wikipedia", "https://wikipedia.com" ],
                  ["google", "https://google.com"]]
        for site in sites:
            
            if f"Open  {site[0]}".lower in query.lower():
                webbrowser.open(site[1])
                say( f"Opening  {site[0]} sir........")
            if "Open music" in query:
                photopath =' C:\Users\sruji\Dropbox\My PC (LAPTOP-K0CAA86I)\Documents\Music'
                os.startfile(photopath)
             if "time" in query:
                 Hour = datetime.datetime.now().strftime("%H")
                 Min = datetime.datetime.now().strftime("%M")

                 say(f"Sir, the time is {Hour} gantala {Min} nimishaaalu")

      