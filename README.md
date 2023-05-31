# Google-ITprofetional-Project1
# Scale and convert images using PIL

Introduction
Your company is in the process of updating its website, and they've hired a design contractor to create some new icon graphics for the site. But the contractor has delivered the final designs in the wrong format -- rotated 90° and too large. Oof! You're not able to get in contact with the designers and your own deadline is approaching fast. You'll need to use Python to get these images ready for launch.

What you'll do
Use the Python Imaging Library to do the following to a batch of images:

Open an image
Rotate an image
Resize an image
Save an image in a specific format in a separate directory

The images received are in the wrong format:

.tiff format
Image resolution 192x192 pixel (too large)
Rotated 90° anti-clockwise
The images required for the launch should be in this format:

.jpeg format

Image resolution 128x128 pixel

Should be straight

Install Pillow
We should change the format and size of these pictures, and rotate them by 90° clockwise. To do this, we'll use Python Imaging Library (PIL). Install pillow library using the following command:

pip3 install pillow
Copied!
Python Imaging Library (known as Pillow in newer versions) is a library in Python that adds support for opening, manipulating, and saving lots of different image file formats.

Pillow offers several standard procedures for image manipulation. These include:

Per-pixel manipulations
Masking and transparency handling
Image filtering, such as blurring, contouring, smoothing, or edge finding
Image enhancing, like sharpening and adjusting brightness, contrast or color
Adding text to images (and much more!)

Write a Python script
This is the challenge section of the lab where you'll write a script that uses PIL to perform the following operations:

Iterate through each file in the folder
For each file:
Rotate the image 90° clockwise
Resize the image from 192x192 to 128x128
Save the image to a new folder in .jpeg format
