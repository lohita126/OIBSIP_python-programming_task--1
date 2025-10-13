import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

# Initialize the speech engine
engine = pyttsx3.init()

def talk(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source, duration=1)
        audio = listener.listen(source)
    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        talk("Network error.")
        return ""

def run_assistant():
    talk("Hello! I'm your assistant. How can I help you?")
    while True:
        command = listen()

        if not command:
            continue

        if "hello" in command:
            talk("Hi there! How can I assist you today?")
        elif "time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The time is {time}")
        elif "date" in command:
            date = datetime.datetime.now().strftime('%A, %B %d, %Y')
            talk(f"Today's date is {date}")
        elif "search" in command:
            topic = command.replace("search", "").strip()
            if topic:
                talk(f"Searching the web for {topic}")
                pywhatkit.search(topic)
            else:
                talk("Please tell me what to search for.")
        elif "exit" in command or "quit" in command:
            talk("Goodbye!")
            break
        else:
            talk("Sorry, I can't perform that task yet.")

# Run the assistant
run_assistant()
