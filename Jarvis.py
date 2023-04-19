
import datetime  
import subprocess  


import pyjokes
import requests
import json
from PIL import Image, ImageGrab
from gtts import gTTS


from pynput import keyboard
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller


from playsound import *  



import os
try:
    import pyttsx3 
except:
    os.system('pip install pyttsx3')
    import pyttsx3 

try :
    import speech_recognition as sr
except:
    os.system('pip install speechRecognition')
    import speech_recognition as sr 

import webbrowser
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)
exit_jarvis = False


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def speak_news():
    url = "http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=yourapikey"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict["articles"]
    speak("Source: The Times Of India")
    speak("Todays Headlines are..")
    for index, articles in enumerate(arts):
        speak(articles["title"])
        if index == len(arts) - 1:
            break
        speak("Moving on the next news headline..")
    speak("These were the top headlines, Have a nice day Sir!!..")


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "yourr-password-here")
    server.sendmail("youremail@gmail.com", to, content)
    server.close()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening !")
    speak("I m Jarvis  ! how can I help you sir")


def takecommand():

    wishme()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.dynamic_energy_threshold = 500
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def voice(p):
    myobj = gTTS(text=p, lang="en", slow=False)
    myobj.save("try.mp3")
    playsound("try.mp3")


def on_press(key):
    if key == keyboard.Key.esc:
        return False  
    try:
        k = key.char  
    except:
        k = key.name  
    if k in ["1", "2", "left", "right"]:  
        
        print("Key pressed: " + k)
        return False  

def on_release(key):
    print("{0} release".format(key))
    if key == Key.esc():
        
        return False

def get_app(Q):
    current = Controller()
    
    if Q == "time":
        print(datetime.now())
        x = datetime.now()
        voice(x)
    elif Q == "news":
        speak_news()

    elif Q == "open notepad":
        subprocess.call(["Notepad.exe"])
    elif Q == "open calculator":
        subprocess.call(["calc.exe"])
    elif Q == "open stikynot":
        subprocess.call(["StikyNot.exe"])
    elif Q == "open shell":
        subprocess.call(["powershell.exe"])
    elif Q == "open paint":
        subprocess.call(["mspaint.exe"])
    elif Q == "open cmd":
        subprocess.call(["cmd.exe"])
    elif Q == "open discord":
        subprocess.call(["discord.exe"])
    elif Q == "open browser":
        subprocess.call(["C:\\Program Files\\Internet Explorer\\iexplore.exe"])
    
    elif Q == "open youtube":
        webbrowser.open("https://www.youtube.com/")  
    elif Q == "open google":
        webbrowser.open("https://www.google.com/")  
    elif Q == "open github":
        webbrowser.open("https://github.com/")
    elif (
        Q == "email to other"
    ):  
        try:
            speak("What should I say?")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)
            to = "abc@gmail.com"
            content = input("Enter content")
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry, I can't send the email.")
    
    
    elif Q == "Take screenshot":
        snapshot = ImageGrab.grab()
        drive_letter = "C:\\"
        folder_name = r"downloaded-files"
        folder_time = datetime.datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
        extention = ".jpg"
        folder_to_save_files = drive_letter + folder_name + folder_time + extention
        snapshot.save(folder_to_save_files)

    elif Q == "Jokes":
        speak(pyjokes.get_joke())

    elif Q == "start recording":
        current.add("Win", "Alt", "r")
        speak("Started recording. just say stop recording to stop.")

    elif Q == "stop recording":
        current.add("Win", "Alt", "r")
        speak("Stopped recording. check your game bar folder for the video")

    elif Q == "clip that":
        current.add("Win", "Alt", "g")
        speak("Clipped. check you game bar file for the video")
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    else:
        exit()

    

    apps = {
        "time": datetime.datetime.now(),
        "notepad": "Notepad.exe",
        "calculator": "calc.exe",
        "stikynot": "StikyNot.exe",
        "shell": "powershell.exe",
        "paint": "mspaint.exe",
        "cmd": "cmd.exe",
        "browser": "C:\\Program Files\Internet Explorer\iexplore.exe",
        "vscode": "C:\\Users\\Users\\User\\AppData\\Local\\Programs\Microsoft VS Code"
    }
    




if __name__ == "__main__":
    while not exit_jarvis:
        Query = takecommand().lower()
        get_app(Query)
    exit_jarvis = True