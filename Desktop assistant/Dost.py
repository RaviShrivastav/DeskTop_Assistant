from venv import main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id) yah hatana hai
engine.setProperty('voice', voices[0].id)
# print('ravi')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Mornning!")
   
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
   
    else:
        speak("Good Evening!")
    
    speak("I am Mahi  Please tell me how may I help you")

def takeCommand():#it takes voice of user through microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1 #agar bolte time gap le to wo us baat ko vhi comeplete n karde
        audio = r.listen(source)

    try:
        print("Recongnizing.....")
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e)
        
        print("Say that again please...")
        return "None"
    return query

           
if __name__ == "__main__":
    # speak("Ravi is a good boy")
    wishME()
    # while True: isse sunta hi rahta hai
    if 1:    
         query = takeCommand().lower()
         
    #logic for exicuting tasks based on query
         if 'wikipedia' in query:
             speak('Searching wikipedia...')
             query = query.replace("wikipedia", "")
             result = wikipedia.summary(query, sentences=2)
             speak("According to wikipedia")
             print(result)
             speak(result)
         
         
         elif'open youtube' in query:
             webbrowser.open("youtube.com")
             
         elif'open google' in query:
             webbrowser.open("google.com")   
             
         elif'open gmail' in query:
             webbrowser.open("gmail.com")     
             
         elif'open stackoverflow' in query:
             webbrowser.open("stackoverflow.com") 
             
         elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir, the time is {strTime}")     
             
         elif 'open vs code' in query:
             codePath = "C:\\Users\\ruchi shrivastav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codePath)
             
        #  elif 'open netflix' in query:
        #      netflixPath = "C:\\Users\\ruchi shrivastav\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
        #      os.startfile(netflixPath)    
        
        
        #  elif 'play  music' in query:
        #      music_dir = 'E:\\Songsnew'
        #      songs = os.listdir(music_dir)
        #      print(songs)
        #      os.startfile(os.path.join(music_dir,song[0])) NOT Working due to directory
        
                  
             
             