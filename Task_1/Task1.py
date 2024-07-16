import os
import cv2 as cv
import numpy as np

def calculate_mean_intensity(img, channel=None):
    if channel is None:
        return round(np.mean(img))
    else:
        return round(np.mean(img[:,:,channel]))

def analyze_image(path):
    try:
        img = cv.imread(path)
        if img is None:
            raise FileNotFoundError
        # print(img,end="")
        
        print(img[:,:,0])
        
        if calculate_mean_intensity(img, 0) == calculate_mean_intensity(img, 1) == calculate_mean_intensity(img, 2):            
            print(f"{img.shape[0]} x {img.shape[1]} pixels")
            print("Colour Channel 1")
            print(f"File Size: {round(os.stat(path).st_size/1024)} KB")
            gray_mean = calculate_mean_intensity(img)
            print(f"Mean Pixel Intensity Gray Scale: {gray_mean}")
            print("Image Type: Gray Scale")
        else:
            print(f"{img.shape[0]} x {img.shape[1]} pixels")
            print(f"Colour Channels: {img.shape[2]}")
            print(f"File Size: {round(os.stat(path).st_size/1024)} KB")
            blue_mean = calculate_mean_intensity(img, 0)
            green_mean = calculate_mean_intensity(img, 1)
            red_mean = calculate_mean_intensity(img, 2)
            print(f"Mean Pixel Intensity (RGB): ({blue_mean}, {green_mean}, {red_mean})")
            print("Image Type: Coloured")
            
    except FileNotFoundError:
        print("Exception occurred: File Not Found")

# Example usage
analyze_image("Photos/ik.png")

