from Voice_input import recognize_speech
from text_processing import process_text
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def calculate(operation, numbers):
    if operation == "add":
        return sum(numbers)
    elif operation == "subtract":
        return numbers[0] - numbers[1]
    elif operation == "multiply":
        return numbers[0] * numbers[1]
    elif operation == "divide":
        try:
            return numbers[0] / numbers[1]
        except ZeroDivisionError:
            return "Cannot divide by Zero"
    else:
        return "Operation not recognized"
    
def main():
    print("Script Started...")
    user_input = recognize_speech()
    if user_input:
        result =process_text(user_input)
        print("Result : ", result)

        if result and result["operation"] and result["numbers"]:
            final_answer = calculate(result["operation"],result["numbers"])
            print(f"final Answer : {final_answer}")
            speak(f"The final answer is {final_answer}")
        else:
            speak("Sorry, I couldn't understand the operation or numbers...")

    else:
        print("I didn't get that")
        speak("Sorry, I couldn't hear you...")


if __name__ == "__main__":
    main()





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