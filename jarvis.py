from pdb import main
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak(" I am Jarvis Sir. Please tell me how may i help you")


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        print (query)


    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
def search_on_youtube(query):
              youtube_search_url = f"https://www.youtube.com/results?search_query={query}"
              webbrowser.open(youtube_search_url)

def search_website_on_google(website_name):
    google_search_url = f"https://www.google.com/search?query={website_name}"
    webbrowser.open(google_search_url)
        

if __name__=="__main__" :
    wishMe()
    while True:
      query = takeCommand().lower()

      # logic for executing tasks based on query
      if 'wikipedia' in query:
          speak('searching wikipedia...')
          query = query.replace("wekipedia", "" )
          results = wikipedia.summary(query, sentences=2)
          speak(results)
      elif 'youtube' in query:
          speak("opening youtube please wait a miniute...")
          search_on_youtube(query)
          
      elif 'google' in query:
           speak("opening Google please wait a miniute...")
           search_website_on_google(query)     