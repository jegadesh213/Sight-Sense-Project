import os
import cv2
import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the recognizer
recognizer = sr.Recognizer()

# Specify the default folder to store captured photos
DEFAULT_FOLDER = "image_folder"

# Function to recognize voice command
def recognize_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

# Function to capture photo and save with the provided name
def capture_and_save(name):
    camera = cv2.VideoCapture(0)
    _, frame = camera.read()
    folder = os.path.join(DEFAULT_FOLDER, name)
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"{name.lower()}.jpg")
    cv2.imwrite(filename, frame)
    print(f"Photo saved as {filename}")
    camera.release()

# Main function
if __name__ == "__main__":
    # Create the default folder if it doesn't exist
    os.makedirs(DEFAULT_FOLDER, exist_ok=True)
    
    while True:
        command = recognize_command()
        if command:
            if "capture" in command:
                parts = command.split()
                if len(parts) > 1:
                    person_name = " ".join(parts[1:])
                    capture_and_save(person_name)
                else:
                    print("Please provide a name after the 'CAPTURE' command.")
            elif "exit" in command:
                print("Quitting...")
                break
