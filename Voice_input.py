print("Script Started...")  # Add this line at the top

import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, couldn't understand what you said 😕")
            return None
        except sr.RequestError:
            print("Error connecting to speech recognition server")
            return None

# Call the function
recognize_speech()
