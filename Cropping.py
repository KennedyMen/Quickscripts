import cv2
import numpy as np

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
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        crop_box = auto_crop(input_path)
        with Image.open(input_path) as img:
            cropped_img = img.crop(crop_box)
            cropped_img.save(output_path)
            print(f"Cropped and saved: {output_path}")
crop_whitespace("/Users/whgf/Library/CloudStorage/GoogleDrive-Wendy@wendyhilliardfoundation.org/Shared drives/WHGF Photo and  Videos/Wendy's Photos and Videos/Old family photos/Freinds copy/JP1 63.png", "/Users/whgf/Library/CloudStorage/GoogleDrive-Wendy@wendyhilliardfoundation.org/Shared drives/WHGF Photo and  Videos/Wendy's Photos and Videos/Old family photos/Cropped /JP1 63.png")
