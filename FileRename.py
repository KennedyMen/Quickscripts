import os
import subprocess
import time

# Path to the folder containing your images
folder_path = "/Users/whgf/Library/CloudStorage/GoogleDrive-Wendy@wendyhilliardfoundation.org/Shared drives/WHGF Photo and  Videos/Wendy's Photos and Videos/Old family photos/Cropped "  # Adjust the path to your images folder

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Filter files to only include image files (you can add more file types as needed)
image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png'))]

# Function to open Quick Look using qlmanage
def open_quicklook(file_path):
    # qlmanage is a command-line tool to display Quick Look previews
    subprocess.Popen(["qlmanage", "-p", file_path])

# Loop through each image and prompt for renaming
for image in image_files:
    if 'Scan' in image:
        file_path = os.path.join(folder_path, image)

        # Open the image in Quick Look using qlmanage
        open_quicklook(file_path)
        
        # Wait for the Quick Look to open (you can adjust this sleep time if necessary)
        time.sleep(1)

        # Prompt for a new name
        new_name = input(f"Current file: {image}. Enter new name (or press Enter to skip): ")

        # If a new name is provided, rename the file
        if new_name:
            new_file_path = os.path.join(folder_path, new_name + os.path.splitext(image)[1])
            os.rename(file_path, new_file_path)
            print(f"Renamed to {new_name + os.path.splitext(image)[1]}")

        # Close Quick Look and proceed to the next file
        print("Closing Quick Look...\n")
        time.sleep(0.5)  # Give some time before proceeding to the next file

        print("Renaming complete.")
