import speech_recognition as aa 
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    instruction = ""  # Define instruction here to avoid NameError
    
    try:
        with aa.Microphone() as origin:
            print("Listening...")
            speech = listener.listen(origin)
            print("Processing...")
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "voiceassistant" in instruction:
                instruction = instruction.replace("voiceassistant", "").strip()
                print("Instruction:", instruction)
            else:
                print("No 'VoiceAssistant' trigger word found.")
    except aa.UnknownValueError:
        print("Could not understand the audio.")
    except aa.RequestError:
        print("Could not request results; check your internet connection.")
    except Exception as e:
        print("Error:", str(e))
    
    return instruction

def play_VoiceAssistant():
    instruction = input_instruction()
    print("Final Instruction:", instruction)
    
    if "play" in instruction:
        song = instruction.replace("play", "").strip()
        talk("Playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is " + time)
    elif "date" in instruction:
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date is " + date)
    elif "how are you" in instruction:
        talk("I am good, how about you?")
    elif "what is your name" in instruction:
        talk("Apologies, I have not been assigned a name yet.")
    elif "who is" in instruction:
        human = instruction.replace("who is", "").strip()
        try:
            info = wikipedia.summary(human, 1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError as e:
            talk("There are multiple results for that name, please be more specific.")
        except wikipedia.exceptions.PageError:
            talk("I couldn't find any information on that topic.")
    else:
        talk("Please repeat")

play_VoiceAssistant()
