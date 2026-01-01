import cv2
import numpy as np

frog = cv2.imread("frog2.jpeg")
if frog is None:
    raise ValueError("Couldn't read")
height, width, color = frog.shape

kernel = np.array([
    [1, 4, 7, 4, 1],
    [4, 16, 26, 16, 4],
    [7, 26, 41, 26, 7],
    [4, 16, 26, 16, 4],
    [1, 4, 7, 4, 1]
], dtype=np.float32) / 273.0

output = np.zeros_like(frog, dtype=np.float32)

for x in range(2, height - 2):
    for y in range(2, width - 2):

        total = 0
        for kx in range(-2, 3):
            for ky in range(-2, 3):
                pixel = frog[x + kx, y + ky]
                weight = kernel[kx + 2, ky + 2]
                total += pixel * weight

        output[x, y] = total

output = np.clip(output, 0, 255).astype(np.uint8)

cv2.imshow("Original", frog)
cv2.imshow("Gaussian Blur (Manual)", output)

cv2.moveWindow("Original", 300, 300)
cv2.moveWindow("Gaussian Blur (Manual)", 700, 300)

cv2.waitKey(0)
cv2.destroyAllWindows()