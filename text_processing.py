print("File is running")
import re

def process_text(text):

    text = text.lower()
    numbers = list(map(int, re.findall(r'\d+', text)))


    if "add" in text or "plus" in text:
        operation ="add"
    elif "subtract" in text or "minus" in text or "difference" in text:
        operation = "subtract"
    elif "multiply" in text or "times" in text or "product" in text:
        operation = "multiply"
    elif "divide" in text or "division" in text or "by" in text:
        operation ="divide"       
    else:
        operation ="Unknown"

    return {
        "operation" : operation,
        "numbers" : numbers
    }    

