def process_text(text):
    print(f"Processing text: {text}")
    return text.lower()

# ✅ This part ensures something actually runs when you execute this file
if __name__ == "__main__":
    sample_input = "What is 5 plus 3?"
    processed = process_text(sample_input)
    print(f"Processed: {processed}")
