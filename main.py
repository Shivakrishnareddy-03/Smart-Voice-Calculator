from Voice_input import recognize_speech
from text_processing import process_text
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    print("Script Started...")
    user_input = recognize_speech()
    if user_input:
        result = process_text(user_input)
        print("Result : ", result)
        speak(f"The result is {result}")
    else:
        print("I didnt got")

if __name__ =="__main__":
    main()