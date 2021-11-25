import cv2

# Initializing the face and eye cascade classifiers from xml files
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Starting the video capture
cap = cv2.VideoCapture(0)
ret, img = cap.read()


# method for getting eyes and smiles from the classifiers
def get_eyes_and_smiles(x, y, w, h):
    roi_face = gray[y:y + h, x:x + w]
    return eye_cascade.detectMultiScale(roi_face, 1.3, 5, minSize=(50, 50)), \
           smile_cascade.detectMultiScale(roi_face, 1.8, 20)


# method to take picture in case all people are smiling and with eyes open
def take_picture(all_faces, current_people=0):
    amount_of_people = len(all_faces)
    if amount_of_people > 0:
        for (xi, yi, wi, hi) in all_faces:
            aux_eyes, aux_smiles = get_eyes_and_smiles(xi, yi, wi, hi)
            if len(aux_eyes) >= 2 and len(aux_smiles) >= 1:
                current_people = current_people + 1
        # if there are
        if current_people == amount_of_people:
            ret, img = cap.read()
            cv2.imshow('img1', img)


while ret:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    # Converting the recorded image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Applying filter to remove impurities
    gray = cv2.bilateralFilter(gray, 5, 1, 1)

    # Detecting the face for region of image to be fed to eye classifier
    faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(200, 200))
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # roi_face is face which is input to eye classifier
            eyes, smiles = get_eyes_and_smiles(x, y, w, h)

            # Examining the length of eyes object for eyes and smile
            if len(eyes) >= 2 and len(smiles) >= 1:
                cv2.putText(img,
                            "Eye and smile detected! Press s to begin",
                            (70, 70),
                            cv2.FONT_HERSHEY_PLAIN, 3,
                            (0, 255, 0), 2)
            # If there are any non-open aye or non-smile
            else:
                # If there are any non-open aye or non-smile show both texts
                if (len(smiles) == 0) and (len(eyes) < 2):
                    cv2.putText(img,
                                "No smile nor eyes detected", (70, 70),
                                cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 2)
                # Text in case there is just no smile
                elif len(smiles) == 0:
                    cv2.putText(img,
                                "No smile detected", (70, 70),
                                cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 2)
                # Text in case there is just blink
                else:
                    cv2.putText(img,
                                "No eyes detected", (70, 70),
                                cv2.FONT_HERSHEY_PLAIN, 3,
                                (0, 0, 255), 2)
    else:
        cv2.putText(img,
                    "No face detected", (100, 100),
                    cv2.FONT_HERSHEY_PLAIN, 3,
                    (0, 255, 0), 2)
    # Controlling the algorithm with keys
    cv2.imshow('detector', img)
    a = cv2.waitKey(1)
    # If press q quit
    if a == ord('q'):
        break
    # If press s take picture
    elif a == ord('s'):
        # This will take the picture
        take_picture(faces)

cap.release()
cv2.destroyAllWindows()
