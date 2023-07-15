import pyttsx3
from pydub import AudioSegment



engine = pyttsx3.init()

def text_to_speech(text):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

# Prompt the user to enter the text
text = input("Enter the text you want to convert to speech: ")

# Call the function to convert the text to speech
text_to_speech(text)


def text_to_speech(text, output_file):
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    
    
    

    # Convert text to speech
    engine.save_to_file(text, output_file)
    engine.runAndWait()

def mp3_converter(input_file, output_file):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Export the audio in MP3 format
    audio.export(output_file, format="mp3")

# Prompt the user to enter the text
text = input("Enter the text you want to convert to speech: ")

# Prompt the user to enter the output filename for speech synthesis
speech_output_file = input("Enter the output filename for speech synthesis (e.g., speech.wav): ")

# Convert the text to speech
text_to_speech(text, speech_output_file)

# Prompt the user to enter the input audio filename for conversion
audio_input_file = input("Enter the input audio filename for conversion (e.g., audio.wav): ")

# Prompt the user to enter the output filename for audio conversion
audio_output_file = input("Enter the output filename for audio conversion (e.g., audio.mp3): ")

# Convert the audio file to MP3
mp3_converter(audio_input_file, audio_output_file)
