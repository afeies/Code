### Colors
- color space: a way to represent a color numerically
    - BGR: OpenCV stores color images as BGR by default, not RGB
- HSV: hue, saturation, value
    - easier than RGB/BGR for color-based object detection
- thresholding: turning an image into a binary decision (keep/reject)
    - in OpenCV, use inRange for color thresholding
- binary mask: an image where pixels are 0 (black) or 255 (white)
    - used to represent where something is detected

### Filtering
- noise: unwanted random pixels/blobs that cause false detections
- morphological operations: binary-image cleanup operations based on a small kernel
    - erosion: shrink white regions, fill small gaps
    - dilation: expand white regions, fill small gaps
    - opening: erosion then dilation (remove small noise)
    - closing: dilation then erosion (fill small holes)
- kernel: the small matrix (e.g., 5x5) used by morphology operations
