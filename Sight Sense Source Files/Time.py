import datetime
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak the current time
def speak_time():
    # Get the current time
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    
    # Convert 24-hour format to 12-hour format with AM/PM
    hour = int(datetime.datetime.now().strftime("%H"))
    if hour >= 12:
        meridiem = "PM"
    else:
        meridiem = "AM"
    if hour > 12:
        hour -= 12

    # Construct the time string
    time_str = f"The current time is {hour}:{datetime.datetime.now().strftime('%M')} {meridiem}"
    
    # Speak out the current time
    engine.say(time_str)
    engine.runAndWait()

if __name__ == "__main__":
    speak_time()
