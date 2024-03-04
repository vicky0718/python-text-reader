import pyttsx3

def text_to_speech(text, speed=150):
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty('voices')

    # Set the desired voice based on gender
    if gender.lower() == 'male':
        engine.setProperty('voice', voices[0].id)  # Male voice
    else:
        engine.setProperty('voice', voices[1].id)  # Female voice

    # Set the speech speed (rate)
    engine.setProperty('rate', speed)

    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    input_text = input("Enter the text you want to convert to speech: ")
    speed = int(input("Enter the speed of speech (default is 150): ") or 150)
    gender_choice = input("Choose voice gender (male/female): ").lower()

    text_to_speech(input_text, speed, gender_choice)
