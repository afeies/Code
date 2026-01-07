import cv2
import numpy as np
import csv
import os
from collections import deque

VIDEO_PATH = "data/ball.MOV"

# tuned HSV bounds
lower = np.array([25, 80, 80])
upper = np.array([45, 255, 255])

kernel = np.ones((5, 5), np.uint8)

# track last n points for drawing the trajectory
trail = deque(maxlen=64)

# save CSV output
os.makedirs("outputs", exist_ok=True)
CSV_PATH = "outputs/trajectory.csv"

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise RuntimeError(f"Cannot open video: {VIDEO_PATH}")

fps = cap.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 30.0 # default to 30 if FPS not available
dt = 1.0 / fps

frame_idx = 0
prev_center = None
prev_t = None

rows = [("frame", "time_s", "x", "y", "speed_px_per_s")] # CSV header

def detect_ball_center(frame):
    # return (center_xy, radius) or (None, None)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        return None, None, mask

    c = max(contours, key=cv2.contourArea)
    area = cv2.contourArea(c)
    if area <= 200:    # ignore tiny blobs, tune if needed
        return None, None, mask

    (x, y), radius = cv2.minEnclosingCircle(c)
    
    if radius < 5:     # ignore tiny circles, tune if needed
        return None, None, mask
    
    return (int(x), int(y)), float(radius), mask

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    t = frame_idx * dt
    
    center, radius, mask = detect_ball_center(frame)
    
    speed = None
    if center is not None:
        # compute speed if we have a previou detection
        if prev_center is not None:
            dx = center[0] - prev_center[0]
            dy = center[1] - prev_center[1]
            dist = (dx * dx + dy * dy) ** 0.5
            speed = dist / dt   # pixels per second
        
        prev_center = center
        prev_t = t
        
        trail.append(center)
        
        # draw current detection
        cv2.circle(frame, center, int(radius), (0, 255, 0), 2)
        cv2.circle(frame, center, 3, (0, 0, 255), -1)
        
        # draw trajectory trail
        for i in range(1, len(trail)):
            cv2.line(frame, trail[i - 1], trail[i], (255, 255, 255), 2)
        
    # overlay text
    txt_speed = "speed: --" if speed is None else f"speed: {speed:.1f}"
    cv2.putText(
        frame,
        f"frame={frame_idx} fps={fps:.1f} {txt_speed}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        (255, 255, 255),
        2,
    )
    
    # save row (use blanks with no detection)
    if center is None:
        rows.append((frame_idx, f"{t:.4f}", "", "", "", ""))
    else:
        rows.append((frame_idx, f"{t:.4f}", center[0], center[1], "" if speed is None else f"{speed:.4f}"))
        
    cv2.imshow("Tracking", frame)
    #cv2.imshow("Mask", mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_idx += 1
    
# write CSV
with open(CSV_PATH, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"Saved: {CSV_PATH}")

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
