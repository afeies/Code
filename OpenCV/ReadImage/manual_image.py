import cv2
import numpy as np

img = np.zeros((8, 8, 3), dtype=np.uint8)

img[0, 0] = [255, 0, 0] # RGB, red?

print(img)

cv2.imshow("8x8 Image", cv2.resize(img, (320, 320), interpolation=cv2.INTER_NEAREST))
cv2.waitKey(0)
cv2.destroyAllWindows()