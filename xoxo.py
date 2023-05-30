import cv2

def detect_faces(image_path):
    # Load the pre-trained face detector (Haar cascade)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))



    # Process each detected face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Extract the face ROI (Region of Interest)
        face_roi = gray[y:y+h, x:x+w]

        # Perform gender and age prediction on the face ROI (replace with your own models or logic)
        gender = predict_gender(face_roi)
        age = predict_age(face_roi)

        # Display the predicted gender and age on the image
        label = f"{gender}, {age}"
        cv2.putText(img, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Show the image with detected faces
    cv2.imshow("Detected Faces", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def predict_gender(face_roi):
    # Replace this with your own gender prediction logic or model
    # Example: return "Male" or "Female"
    gender = "Male"  # Placeholder for the predicted gender
    return gender

import random

def predict_age(face_roi):
    # Replace this with your own age prediction logic or model
    # Example: return an integer representing the predicted age
    
    # Define the age ranges and their corresponding predicted ages
    age_ranges = [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 100)]
    predicted_ages = [8, 15, 25, 35, 45, 55, 80]
    
    # Randomly select an age range
    index = random.randint(0, len(age_ranges) - 1)
    
    # Get the predicted age within the selected age range
    age_range = age_ranges[index]
    predicted_age = random.randint(age_range[0], age_range[1])
    
    return predicted_age



#use example
image_path = 'C:/Users/pc/Pictures/Camera Roll/WIN_20221210_11_00_01_Pro.jpg'
detect_faces(image_path)