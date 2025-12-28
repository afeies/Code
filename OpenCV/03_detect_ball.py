import cv2
import numpy as np

VIDEO_PATH = "data/ball.MOV"

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise RuntimeError(f"Cannot open video: {VIDEO_PATH}")

# start with adjusted HSV bounds
# adjust these if needed

lower = np.array([25, 80, 80])      # H, S, V
upper = np.array([45, 255, 255])

# kernel for cleaning noise in the mask
kernel = np.ones((5, 5), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    
    # clean the mask
    # remove small specs and fill small holes
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) # fill holes
    
    # find contours on the binary mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # pick the largest contour
        c = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(c)
        
        # ignore tiny blobs
        if area > 200:    # tune this threshold if needed
            (x, y), radius = cv2.minEnclosingCircle(c)
            
            # ignore tiny circles
            if radius > 5:    # tune this threshold if needed
                center = (int(x), int(y))
                
                # draw detection
                cv2.circle(frame, center, int(radius), (0, 255, 0), 2)
                cv2.circle(frame, center, 3, (0, 0, 255), -1)
                cv2.putText(
                    frame,
                    f"area={int(area)} r={radius:.1f}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0,
                    (255, 255, 255),
                    2,
                )
            
        # show frame + mask for debugging
        cv2.imshow("Detection", frame)
        # cv2.imshow("Mask", mask)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows() 
        
        
