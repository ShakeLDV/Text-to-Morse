from data import morse

def convert_to_morse(text):
    morse_text = [morse.get(i) for i in text]
    morse_text = " ".join(morse_text)
    return morse_text
        
        
running = True

while running:
    text_to_convert = input("What sentence do you want to convert to morse code? (type exit to quit) ").upper()
    if text_to_convert == "EXIT":
        running = False
        continue
    usable_text = list(text_to_convert)

    print(f"Here is your translation: {convert_to_morse(usable_text)}")
