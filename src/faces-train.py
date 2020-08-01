import os
import cv2
import numpy as np
from PIL import Image
import pickle

# Get the base directory of current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Append images to path
image_dir = os.path.join(BASE_DIR, "images")

# Need to import faec cascades to find region of interest
face_cascade = cv2.CascadeClassifier("cascades/data/haarcascade_frontalface_alt2.xml")

# Initialize the recognizer we will be using
recognizer = cv2.face.LBPHFaceRecognizer_create() 


current_id = 0
label_ids = {} # Dictionary to associate labels to training data

x_train = [] # The images to be used as training data
y_labels = [] # The labels we will associate with the training data

# Traversee the image directory to get the labels
for root, dirs, files in os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):


			# Path of the image file
			path = os.path.join(root, file)
			# The labels will just be the name of the directories
			label = os.path.basename(root).replace(" ", "-").lower()
			#print(label, path)

			# Add a label id to the labels
			if not label in label_ids: # label is in dictionary
				label_ids[label] = current_id
				current_id += 1

			id_ = label_ids[label]
			#print(label_ids)

			# y_labels.append(label) # Want a number value for a label 
			# x_train.append(path) # Verify with image and turn into numpy array in gray

			# Open & convert to grayscale
			pil_image = Image.open(path).convert("L") 

			# Resize image for better training data
			size = (550, 550)
			final_image = pil_image.resize(size, Image.ANTIALIAS)

			# Turn every pixel of the image into a numpy array
			# We want to train on the number of this array
			image_array = np.array(pil_image, "uint8")
			#print(image_array)

			# Detect all the faces in the image
			faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

			for (x,y,w,h) in faces:
				roi = image_array[y:y+h, x:x+w]
				x_train.append(roi) # we want to associate label to this training data
				y_labels.append(id_) # A number associated with each labels

# Save label ids to a pickle file
with open("labels.pkl", "wb") as f:
	pickle.dump(label_ids,f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")