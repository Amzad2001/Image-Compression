import tinify
# import os
from pathlib import Path

# Set your API key
tinify.key = 'qSdw1rRgYcNWTrYm0lYHmfYFYh1KptFy'

# Specify the source folder with images and the destination folder
source_folder = Path('C:\\pract\\images')
destination_folder = Path('C:\\pract\\aftercompressed')

# Create the destination folder if it doesn't exist
# os.makedirs(destination_folder, exist_ok=True)

# Function to compress and save images
def compress_and_save(image_path):
    # try:
        # Define the destination path 
        destination_path = destination_folder / image_path.name
        # Use the tinify API to compress the image and save it
        source = tinify.from_file(str(image_path))
        source.to_file(str(destination_path))
        print(f"Compressed and saved {image_path.name}")
    # except tinify.Error as e:
    #     # Error handling here
    #     print(f"An error occurred while compressing {image_path.name}: {e}")

# Loop through all PNG and JPG images in the source folder
for file_type in ['*.png', '*.jpg']:
    for image_path in source_folder.glob(file_type):
        compress_and_save(image_path)
