# GUI Projects using Python

This repository contains several projects that demonstrate the use of GUI (Graphical User Interface) frameworks in Python.

The projects include a **photo editor**, a **simple calculator**, an **image classifier**, and a **camera reader**. 

Each project demonstrates different features and technologies such as PyQt5, OpenCV, and Tkinter. 

These projects can be useful for beginners who want to learn and explore the capabilities of these frameworks.

---
# Table of Contents

- [Photo editor](#photo-editor)
- [Calculator](#calculator)
- [ClassifyImages](#classifyimages)
- [Camera Reader](#camera-reader)

---

## Photo editor

![GUI_Image](./photo%20editor.png)

This project is a simple photo editor using Python, PyQt5, and OpenCV. The
editor allows the user to load an image, change the brightness and blur,
and save the image.

### How to use

1. Clone this repository.
2. Install the requirements.
3. Run `python photo_editor.py`
4. Click on the "Open" button to load an image.
5. Adjust the slider to change the brightness and blur.
6. Click on the "Save" button to save the image.

### Implemented features

- Load an image.
- Change brightness and blur of the image.
- Save the modified image.

### Technologies used

- Python
- PyQt5
- OpenCV

---

## Calculator
![simple calculator](./simple%20calculator.png)

This is a simple calculator application built using the Tkinter library in Python. It allows users to perform basic arithmetic operations such as addition, subtraction, and getting the result of an equation.

### Usage

To run the calculator, follow these steps:

1. Execute the `calculator.py` file.
2. The application will open with an empty display.
3. Enter numbers by clicking on the corresponding buttons (0-9).
4. Perform an operation by clicking on the "+" button to add numbers, the "-" button to subtract numbers, or the "=" button to get the result of the entered equation.
5. Clear the display by clicking on the "C" button.

### Technologies Used

- Python
- Tkinter

---

## ClassifyImages

![image classifier](./Image%20Classifier.png)

This is a GUI application for classifying and manipulating images using PyQt5 and OpenCV.

This gui was used for saving images in specific folders which was used in collecting data for taining **Deep Learning Classification Model**.

The project was mainly for devoloping a **autonomous driving ROV** which can process the input frame to predict the movement according to the seen line.

The main movement directions are:

- Up
- Down
- Right

### Features

- Display images from a folder
- Navigate through images using forward and backward buttons
- Save manipulated images to specific folders

### Usage

1. Run the `ClassifyImages.py` script:

    ```bash
    python ClassifyImages.py
    ```

2. The GUI application will open, displaying the first image in the specified folder.

3. Use the forward and backward buttons to navigate through the images.

4. Click on the various manipulation buttons to perform image operations.

5. Click the "SHOW" button to display the current image without any manipulation.

6. Close the application when done.

---

## Camera Reader

This project is a simple Python application that uses OpenCV and PyQt5 to display a live video feed from a webcam. It demonstrates the use of multithreading and signals/slots to update the UI in real-time.

### Usage

1. Clone this repository.
2. Install the requirements.
3. Run `python camera_reader.py`
4. The application will open and display the live video feed from the webcam.
5. Close the application when done.
