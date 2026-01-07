import cv2

frog = cv2.imread("frog2.jpeg")

if frog is None:
    raise ValueError("Couldn't read")

blurredFrog = cv2.GaussianBlur(frog, (5, 5), 0)
kernel = cv2.getGaussianKernel(5, 0)
newKernel = kernel @ kernel.T
print(newKernel)

cv2.imshow("Original", frog)
cv2.imshow("Blurred", blurredFrog)

cv2.moveWindow("Original", 300, 300)
cv2.moveWindow("Blurred", 700, 300)

cv2.waitKey(0)
cv2.destroyAllWindows()