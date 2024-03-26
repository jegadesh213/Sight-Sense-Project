import os
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to execute the Python script
def run_python_script(script_name):
    try:
        os.system(f"python {script_name}")
    except Exception as e:
        print("Error:", e)

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
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

# Main function
if __name__ == "__main__":
    # Get the list of Python files in the current directory
    python_files = [file for file in os.listdir() if file.endswith(".py")]

    if not python_files:
        print("No Python files found in the current directory.")
        exit()

    print("Python files found in the current directory:")
    for i, file in enumerate(python_files, 1):
        print(f"{i}. {file}")

    while True:
        # Recognize the voice command
        command = recognize_command()

        # Check if the command is empty (user pressed Enter)
        if not command:
            continue

        # Check if the command is "quit" to exit the loop
        if command == "exit":
            print("Quitting...")
            break

        # Check if the command matches any of the Python files
        for i, file in enumerate(python_files, 1):
            if command.lower() in file.lower():
                print(f"Running {file}...")
                run_python_script(file)
                break
        else:
            print("Python file not found for the given command.")
