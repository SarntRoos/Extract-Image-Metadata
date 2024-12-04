## This Python script allows you to extract and display metadata from image files in a specified folder. It uses the Pillow (PIL) library for basic image processing and ExifRead for extracting EXIF metadata from JPEG files.

## Features 🛠️
- **File Information**: Displays file format, size (width x height), and color mode.
- **EXIF Metadata**:
  - Extracts EXIF metadata for JPEG images.
  - Skips EXIF processing for non-JPEG files.
- **Folder Scanning**: Processes all images in a folder, including `.png`, `.jpg`, `.jpeg`, `.tiff`, `.bmp`, and `.gif`.

---

## How It Works ⚙️
### Input Folder Path:
- Prompts the user to input the folder path containing the images.
- Checks if the folder exists; exits with an error message if it doesn’t.

### File Processing:
- Iterates through all supported image files in the folder.
- Extracts and prints metadata, including basic information and EXIF data (if available).

### Error Handling:
- Gracefully handles errors during processing, providing informative messages.

---

### Requirements:
- Pillow==9.4.0
- ExifRead==2.3.2

## Installation 🚀
1. Clone the repository:
   ```bash
   git clone https://github.com/SarntRoos/extract-image-metadata.git
