import cv2
import numpy as np

VIDEO_PATH = "data/ball.MOV"

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise RuntimeError(f"Cannot open video: {VIDEO_PATH}")

# ball is around yeelow-green
# guess and tune numbers
lower = np.array([25, 80, 80])      # H, S, V
upper = np.array([45, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    
    # show only the masked pixels on the original frame
    masked_view = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow("Original", frame)
    cv2.imshow("Mask (white = detected color)", mask)
    cv2.imshow("Masked view", masked_view)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()