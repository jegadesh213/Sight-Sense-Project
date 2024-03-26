import geocoder
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak the user's location
def speak_location():
    # Get the user's location based on IP address
    location = geocoder.ip('me')
    
    # Construct the location string
    location_str = f"You are currently in {location.city}, {location.state}, {location.country}"
    
    # Speak out the location
    engine.say(location_str)
    engine.runAndWait()

if __name__ == "__main__":
    speak_location()
