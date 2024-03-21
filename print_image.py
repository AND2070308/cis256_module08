"""
Andrew Woodward
Module 08 Lab Assignment
Part B

This program prints a cat image as text.
"""
from PIL import Image

IMAGE_FILE='cat.png'
image = Image.open(IMAGE_FILE).convert("1")  # Convert to 1-bit black and white

# Get the image dimensions
width, height = image.size

# Iterate pixels and print the corresponding character
for y in range(height):
    for x in range(width):
        pixel_value = image.getpixel((x, y))
        # print lines without automatic newline
        # Source: https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
        if pixel_value == 0:  # Black
            print("*", end="")
        else:  # White pixel
            print(" ", end="")
    print()  # Move to next line