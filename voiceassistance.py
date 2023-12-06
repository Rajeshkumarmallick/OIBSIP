import speech_recognition as sr
import pyttsx3
import wikipedia

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en')
        print(f"You: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please try again.")
        return ""
    except sr.RequestError as e:
        print(f"Error accessing Google Speech Recognition service: {e}")
        return ""

def assistant(query):
    if "hello" in query:
        speak("Hi there! How can I assist you?")
    elif "your name" in query:
        speak("I am a voice assistant created by ChatGPT.")
    elif "Wikipedia" in query:
        query = query.replace("Wikipedia", "")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(f"Wikipedia says: {result}")
        except wikipedia.DisambiguationError as e:
            speak("There are multiple options. Can you be more specific?")
        except wikipedia.PageError as e:
            speak("I couldn't find any information on that topic.")
    elif "quit" in query or "exit" in query:
        speak("Goodbye! Have a great day.")
        exit()
    else:
        speak("I'm sorry, I didn't understand that.")

def main():
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        query = listen().lower()

        if query:
            assistant(query)

if __name__ == "__main__":
    main()
