
#USING YOLO 
import cv2
from ultralytics import YOLO
from playsound import playsound
import winsound
import time
import threading

# Load YOLO model
model = YOLO('yolov8n.pt')  


# person limit, threshold (can be changed)
MAX_PERSONS = 5
alerted = False  # To prevent repeat alert


# Function to play beep (Using winbeep)
def play_beep():
    winsound.Beep(1000, 500)


# Function to play beep
# def play_beep():
#     playsound("beep.mp3")

# Function to play voice
# def play_voice():
#     playsound("alert.mp3")


# Open camera 
cap = cv2.VideoCapture("assets/stock2.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)[0]
    person_count = 0

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        class_id = int(class_id)

        if model.names[class_id] == "person":
            person_count += 1
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

    # Show person count on screen
    cv2.putText(frame, f"People: {person_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 2)

    # Alert if over capacity
    if person_count > MAX_PERSONS:
        cv2.putText(frame, "Overloaded! Please wait.", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        if not alerted:
            threading.Thread(target=play_beep).start()
            alerted = True
    else:
        alerted = False

    # Display frame
    cv2.imshow("Smart Elevator", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
