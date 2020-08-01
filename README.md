# Facial Indentification

This project does both facial identification and recognition. When a familiar face is put in front of the camera, the program writes the message "Hello [name]". If another face is in front of the camera, it writes "New member" on the video frame. The script *faces-learn.py* also allows for learning new faces.

## Getting Started
Make sure you have a copy of Python 3 running on your system and OpenCV installed

### Packages

OpenCV will need to be instlled on the system (both main and contrib modules), as well as pillow and numpy:
```
pip install opencv-contrib-python 
pip install numpy
pip install pillow
```

## Running the program

### Step 1) Get Training Data
The first step to running the program is to provide some faces of the particular person you want to recognize.

This can be done by places images of your face into the */images/[name]* folder, where the name of the folder is the name of the person you want to recognize.

Alternatively, you can run the the script *faces-learn.py*. Provide the name of the member you want to add, and then let the program run approximately 30 seconds take photos of your face to learn from. To exit either press *Ctrl-C* at the terminal or *'q'* in the OpenCV window.

### Step 2) Create a Model
Once finish, run the script *faces-train.py* to generate a model

### Step 3) Facial Detection
The last step is to run the script faces.py.

This will say "Hello [name]" if you are a member of the system, or "New member" if you are not recognized.

## Acknowledgments and Helpful Links

https://docs.opencv.org/4.3.0/db/d28/tutorial_cascade_classifier.html

https://www.youtube.com/playlist?list=PLEsfXFp6DpzRyxnU-vfs3vk-61Wpt7bOS




