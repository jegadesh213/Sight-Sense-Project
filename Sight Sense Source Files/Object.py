import cv2
import numpy as np
import pyttsx3
import os

# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Check if the model is loaded successfully
if net.empty():
    print("Failed to load YOLO model")
    exit()

# Load class names
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Specify the output layer names
output_layer_names = ["yolo_82", "yolo_94", "yolo_106"]

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to perform object detection and speak out detected object
def detect_objects_and_speak(frame):
    # Detecting objects
    height, width, channels = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layer_names)

    # Showing information on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y + 30), font, 3, (0, 255, 0), 3)

            # Speak out the detected object
            engine.say(label)
            engine.runAndWait()

            # Check if the detected object is a person
            if label.lower() == 'person':
                # Redirect to Person.py for face recognition
                os.system("python Person.py")
                return  # Exit the function to prevent further processing

    # Display the frame with object detection
    cv2.imshow('Object Detection', frame)
    cv2.waitKey(1)

# Open webcam
cap = cv2.VideoCapture(0)

# Start object detection loop
while True:
    ret, frame = cap.read()
    detect_objects_and_speak(frame)

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
