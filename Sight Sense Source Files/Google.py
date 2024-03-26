import speech_recognition as sr
import webbrowser
import pyttsx3

def search_google(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def recognize_command():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()

    with sr.Microphone() as source:
        print("Listening for search query...")
        engine.say("Listening for search query...")
        engine.runAndWait()
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        engine.say("You said: " + query)
        engine.runAndWait()
        return query
    except sr.UnknownValueError:
        print("Could not understand audio")
        engine.say("Could not understand audio")
        engine.runAndWait()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        engine.say("Could not request results")
        engine.runAndWait()

if __name__ == "__main__":
    while True:
        command = recognize_command()
        if command:
            search_google(command)
            break
