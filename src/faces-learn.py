import cv2
import os
import time # Used to name images 

# Covers front-of-face classification, needed to detect face
face_cascade = cv2.CascadeClassifier("cascades/data/haarcascade_frontalface_alt2.xml")

cap = cv2.VideoCapture(0)

# Assign the path to the current working directory
path = os.getcwd()
print(path)

new_member_name = input("What will the new member's name be? ")
imwrite_path = os.path.join(path,"images", new_member_name) # The path where the images will be writen

try:
    os.mkdir(imwrite_path)
except OSError:
    print ("Creation of the directory %s failed" % imwrite_path)
else:
    print ("Successfully created the directory %s " % imwrite_path)


#test = input("test")

os.chdir(imwrite_path) # Change the directory to where the images will be saved

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
		print(x,y,w,h) # Print regions of interest
		roi_gray = gray[y:y+h, x:x+w] # The square region of interest of face
		roi_color = frame[y:y+h, x:x+w] # Region of interest in color frame

		img_item = str(time.time()).replace(".","")+".png" # name of the image  
		#img_item = str(int(time.time()))+".png"
		#imwrite_path = "images/"+new_member_name+"/"
		cv2.imwrite(img_item, frame) # Save the image


		# Write label text on the video
		# Can put inside a function
		font = cv2.FONT_HERSHEY_SIMPLEX
		name = "Learning Face... "
		color = (255, 255, 255)
		stroke = 2
		cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)

		color = (255, 0, 0) # BGR, the color of the rectangle
		stroke = 2 # The thickness of the rectangle
		end_coord_x = x + w
		end_coord_y = y + h
		# Draw on the frame
		cv2.rectangle(frame, (x, y), (end_coord_x, end_coord_y), color, stroke) 
	# Display the frame
	cv2.imshow("frame", frame)
	# time.sleep(1) # Pause a second before attempting to save next image

	# Exit the program
	if cv2.waitKey(20) & 0xFF == ord("q"):
		break

cap.release()
cv2.destroyAllWindows()