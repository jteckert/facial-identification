import cv2
import pickle

# Covers front-of-face classification, needed to detect face
face_cascade = cv2.CascadeClassifier("cascades/data/haarcascade_frontalface_alt2.xml")

# Initialize the recognize we will be using
recognizer = cv2.face.LBPHFaceRecognizer_create() 

# Import the trained data
recognizer.read("trainner.yml")

labels = {}
with open("labels.pkl", "rb") as f:
	original_labels = pickle.load(f)
	labels = {v:k for k,v in original_labels.items()} # Inverse the dictionary

cap = cv2.VideoCapture(0)

while True:
	# Capture each frame
	ret, frame = cap.read()

	# For the cascade to work, the frame must be in gray
	# Convert to gray
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect all the faces in the frame
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

	# Iterate through the detected faces
	for(x, y, w, h) in faces:
		#print(x,y,w,h) # Print regions of interest
		roi_gray = gray[y:y+h, x:x+w] # The square region of interest of face
		roi_color = frame[y:y+h, x:x+w] # Region of interest in color frame

		# Recognize
		id_, conf = recognizer.predict(roi_gray) # The label and confidence

		print(conf)
		if conf >= 40 and conf <= 85: # Confidence range 
			print(id_)
			print(labels[id_])

			# Write label text on the video
			# Can put inside a function
			font = cv2.FONT_HERSHEY_SIMPLEX
			name = "Hello "+labels[id_]
			color = (255, 255, 255)
			stroke = 2
			cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
		else: # If the face is not recognizable within the confidence range, do this
			# Write label text on the video
			font = cv2.FONT_HERSHEY_SIMPLEX
			name = "New member"
			color = (255, 255, 255)
			stroke = 2
			cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)

		# img_item = "my-image.png" 
		# cv2.imwrite(img_item, roi_gray) # Save just the face

		color = (255, 0, 0) # BGR, the color of the rectangle
		stroke = 2 # The thickness of the rectangle
		end_coord_x = x + w
		end_coord_y = y + h
		# Draw on the frame
		cv2.rectangle(frame, (x, y), (end_coord_x, end_coord_y), color, stroke) 
	# Display the frame
	cv2.imshow("frame", frame)

	# Exit the program
	if cv2.waitKey(20) & 0xFF == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()