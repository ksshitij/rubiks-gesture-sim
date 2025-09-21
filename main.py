"""
Rubik's Cube Gesture Simulator – Early Demo
Uses OpenCV to capture webcam frames and a placeholder for gesture recognition.
"""

import cv2

cap = cv2.VideoCapture(0)
print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.putText(frame, "Gesture detection not implemented yet",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
    cv2.imshow("Rubik's Gesture Simulator", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
