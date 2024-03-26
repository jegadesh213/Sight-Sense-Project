import cv2
import numpy as np
import os
import pyttsx3

# Function to load images and labels from a directory
def load_images_from_folder(folder):
    images = []
    labels = []
    label_dict = {}
    idx = 0
    for filename in os.listdir(folder):
        label_dict[idx] = filename.split(".")[0]  # Map label index to person name
        for img_file in os.listdir(os.path.join(folder, filename)):
            img_path = os.path.join(folder, filename, img_file)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                images.append(img)
                labels.append(idx)
        idx += 1
    return images, np.array(labels), label_dict

# Load images and labels
images, labels, label_dict = load_images_from_folder('image_folder')

# Train face recognizer model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(images, labels)

# Function to recognize faces from webcam and speak out the name
def recognize_faces_and_speak():
    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Start capturing video from the webcam
    camera = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        _, frame = camera.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Predict the label of the face
            label, _ = recognizer.predict(gray[y:y+h, x:x+w])

            # Get the name corresponding to the predicted label
            name = label_dict.get(label, "Unknown")

            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display the name of the recognized face below the box
            cv2.putText(frame, name, (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

            # Speak out the name
            engine.say(name)
            engine.runAndWait()

        # Display the frame
        cv2.imshow('Face Recognition', frame)

        # Press 'Enter' key to exit the loop
        if cv2.waitKey(1) == 13:  # 13 is the ASCII code for the Enter key
            break

    # Release the camera and close all OpenCV windows
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Load Haar cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Start face recognition and speak out the name
    recognize_faces_and_speak()

