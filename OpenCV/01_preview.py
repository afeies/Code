import cv2

VIDEO_PATH = "data/ball.MOV"

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    raise RuntimeError(f"Cannot open video: {VIDEO_PATH}")

fps = cap.get(cv2.CAP_PROP_FPS)
frame_idx = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break # End of video
    
    # Overlay frame index + fps
    cv2.putText(
        frame,
        f"frame={frame_idx} fps={fps:.2f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )
    
    cv2.imshow("Preview", frame)
    
    # 1 ms wait; press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    frame_idx += 1
    
cap.release()
cv2.destroyAllWindows()