from PIL import Image
import os
import cv2
import numpy as np

# Folder containing the images
input_folder = "/Users/whgf/Downloads/New scans "
output_folder = "/Users/whgf/Downloads/New Crops"
def crop_whitespace(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Use adaptive thresholding to detect non-white areas
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Get the bounding box of the largest contour
    x, y, w, h = cv2.boundingRect(max(contours, key=cv2.contourArea))
    
    # Crop the image to the bounding box
    cropped = image[y:y+h, x:x+w]
    
    # Save the cropped image
    cv2.imwrite(output_path, cropped)
    print(f"Cropped image saved to {output_path}")
# Example usage
# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        input_pathx = os.path.join(input_folder, filename)
        output_pathx = os.path.join(output_folder, filename)
        crop_whitespace(input_pathx, output_pathx)
        print(f"Cropped and saved: {output_pathx}")
