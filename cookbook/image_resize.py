# Generate by ChatGPT Gemini-1.5 Flash
# write a pyhon programe to resize all image in a folder to long size max to 1024px, and save the reized image to another folder

from PIL import Image
import os
import argparse

def resize_images(source_folder, destination_folder):
    """Resizes images in a folder, limiting the longest side to 1024px."""

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')): # Add more extensions if needed
            continue

        filepath = os.path.join(source_folder, filename)
        try:
            with Image.open(filepath) as img:
                width, height = img.size

                # Determine scaling factor
                if width > height:
                    scale_factor = 1024 / width
                else:
                    scale_factor = 1024 / height

                new_width = int(width * scale_factor)
                new_height = int(height * scale_factor)

                resized_img = img.resize((new_width, new_height), Image.LANCZOS) #LANCZOS for better quality

                destination_filepath = os.path.join(destination_folder, filename)
                resized_img.save(destination_filepath)
                print(f"Resized and saved: {filename}")

        except IOError as e:
            print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize images in a folder.")
    parser.add_argument("source_folder", help="Path to the source folder containing images")
    parser.add_argument("destination_folder", help="Path to the destination folder for resized images")
    args = parser.parse_args()

    resize_images(args.source_folder, args.destination_folder)