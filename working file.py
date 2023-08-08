import speech_recognition as sr
import os
import webbrowser
import datetime
import subprocess
import openai
import random
import pyttsx3

def ai(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    text = f"OpenAI response for prompt: {prompt}\n***********\n\n"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0].text)
    text += response.choices[0].text
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    file_name = f"prompt-{random.randint(1, 23344323455)}.txt"
    with open(file_name, "w") as f:
        f.write(text)


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print('Spyder')
    say("Hello, I am Jarvis AI")
    while True:
        print("Listening")
        query = takeCommand()
        sites = [["Youtube", "https://www.youtube.com"], ["wikipedia", "https://wikipedia.com"],
                 ["google", "https://google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                webbrowser.open(site[1])
                say(f"Opening {site[0]} sir........")
        if "Open music".lower() in query.lower():
            musicpath = r"C:\Users\sruji\Dropbox\My PC (LAPTOP-K0CAA86I)\Documents\Music"
            subprocess.Popen(['explorer', musicpath])  # Open music folder in default file explorer
        if "Open Brave".lower() in query.lower():
            musicpath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk"
            subprocess.Popen(['explorer', musicpath])
        if "time" in query:
            Hour = datetime.datetime.now().strftime("%H")
            Min = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {Hour} gantala {Min} nimishaaalu")
        if "Using AI".lower() in query.lower():
            ai(prompt=query)
