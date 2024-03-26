import cv2
import pytesseract
import pyttsx3

def recognize_text_from_webcam():
    # Start capturing video from the webcam
    camera = cv2.VideoCapture(0)

    # Set up text-to-speech engine
    engine = pyttsx3.init()

    while True:
        # Capture frame-by-frame
        _, frame = camera.read()

        # Convert the frame to grayscale (optional)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Use pytesseract to recognize text from the frame
        text = pytesseract.image_to_string(gray)

        # Display the captured frame with recognized text
        cv2.imshow('Text Recognition', frame)

        # Convert recognized text to speech
        engine.say(text)
        engine.runAndWait()

        # Press 'Enter' key to exit the loop
        if cv2.waitKey(1) == 13:  # 13 is the ASCII code for the Enter key
            break

    # Release the camera and close all OpenCV windows
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    recognize_text_from_webcam()

