from PIL import Image
import exifread
import os

def extract_metadata(image_path):
    try:
        # Open the image using PIL
        with Image.open(image_path) as img:
            print(f"--- Metadata for {os.path.basename(image_path)} ---")
            print(f"File Format: {img.format}")
            print(f"Image Size: {img.size} (Width x Height)")
            print(f"Color Mode: {img.mode}")
        
        # Skip EXIF processing for non-JPEG files
        if img.format != 'JPEG':
            print("\nSkipping EXIF metadata processing (not a JPEG file).")
            print("-" * 50)
            return
        
        # Use exifread for JPEG files
        with open(image_path, 'rb') as img_file:
            tags = exifread.process_file(img_file)
            if tags:
                print("\nEXIF Metadata:")
                for tag, value in tags.items():
                    print(f"{tag}: {value}")
            else:
                print("\nNo EXIF metadata found.")
            print("-" * 50)
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def main():
    folder_path = input("Enter the folder path containing images: ").strip()
    
    if not os.path.exists(folder_path):
        print("The specified folder does not exist.")
        return

    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, file_name)
            extract_metadata(image_path)

if __name__ == "__main__":
    main()
