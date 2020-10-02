import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):

#It speaks the given string as output
    newVoiceRate=150
    engine.setProperty('rate',newVoiceRate)
    engine.say(audio)
    engine.runAndWait()

def wishme():


#It wishes the user as per the time


    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")
        engine.runAndWait()

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")

    elif hour>=16 and hour<20:
        speak("Good Evening!")

    else:
        speak("Good Night!")

    speak("Hello. I'm Jarvis. How may I help u?")


def takecommand():
#It takes microphone input and returns string output
    r = sr.Recognizer()
    with  sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("Please say that again...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
    #Logic for executing tasks
        if  'what is' in query:
            speak("Searching...")
            query = query.replace("What is","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to google")
            print(results)
            speak(results)
        elif 'play music' in query:
            music_dir = "D:\\Music\\Favourite"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the current time is: {strtime}")
        elif 'open' in query:
             url = query.replace('open', " ")
             speak(f"opening for you, {url}")
             webbrowser.open(url)
        elif 'open youtube' in query: 
            speak("Here you go to Youtube\n") 
            webbrowser.open("youtube.com")
        elif 'send a mail' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                speak("whome should i send") 
                to = input()     
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email")            
        elif 'get lost' in query:
            speak("Goodbye boss.")
            exit()
