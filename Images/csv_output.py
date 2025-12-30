import cv2
import csv

img = cv2.imread("frog.png")

with open("frog_pixels.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["row", "col", "B", "G", "R"])

    for row in range(32):
        for col in range(32):
            B, G, R = img[row, col]
            writer.writerow([row, col, B, G, R])