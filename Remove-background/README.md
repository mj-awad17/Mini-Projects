# StreamLit-App-Background-Remover

[![Watch the video](https://github.com/mj-awad17/StreamLit-App-Background-Remover/assets/77524488/3d296849-de31-41c3-a558-e2182ac0af0e)](https://github.com/mj-awad17/StreamLit-App-Background-Remover/assets/77524488/3d296849-de31-41c3-a558-e2182ac0af0e)

---
This project is a web application built using Streamlit that allows users to upload images and remove their backgrounds using the rembg library. The app provides a simple and interactive interface for users to manipulate images and download the processed results.

## Features
- Image Upload: Users can upload images in PNG, JPG, or JPEG formats.
- Background Removal: The app utilizes the rembg library to remove backgrounds from uploaded images.
- Image Resizing: The processed images are resized for better viewing and download.
- Download Option: Users can download the processed images with the background removed.

## Requirements
To run this application, you will need the following:

- Python 3.x
- Streamlit
- rembg
- Pillow

You can install the required libraries using pip:

```
pip install streamlit rembg Pillow
```
## How to Run the App
1. Clone this repository or download the script.
2. Navigate to the directory where the script is located.
3. Run the following command in your terminal:

```
streamlit run app.py
```
4. Open your web browser and go to http://localhost:8501 to access the app.

## Usage Instructions
1. Click on the "Upload an image" button to select an image file from your computer.
2. The original image will be displayed along with the processed image with the background removed.
3. Click on the "Download Image" button to save the processed image to your local machine.

## Troubleshooting
If you encounter any issues, please ensure that:

- You have installed all required libraries.
- The image formats are supported (PNG, JPG, JPEG).
- If the issue persists, check the error message displayed in the app for more information.

### License
This project is open-source and available under the MIT License. Feel free to modify and distribute it as you wish.
---
