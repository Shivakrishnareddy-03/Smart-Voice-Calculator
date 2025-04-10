import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening....")
        audio = recognizer.listen(source)
        print("🎤 Recognizing....")
    try:
        text = recognizer.recognize_google(audio, language='en-US')
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("🤷 Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("🤖 Sorry, there was an error with the speech recognition service.")
        return None
