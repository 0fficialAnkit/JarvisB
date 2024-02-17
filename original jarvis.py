import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """Function to convert text to speech"""
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis. How may I assist you?")


def take_command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return None
    return query


if __name__ == "__main__":
    wish_me()

    while True:
        query = take_command()

        if query:
            query = query.lower()

            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("https://www.youtube.com")

            elif 'open google' in query:
                webbrowser.open("https://www.google.com")

            elif 'play music' in query:
                music_dir = 'C:\\Path\\to\\music\\folder'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'what time is it' in query:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {current_time}")

            elif 'quit' in query:
                speak("Goodbye!")
                exit()
