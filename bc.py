import dlib
from PIL import Image
from skimage import io
import matplotlib.pyplot as plt
import cv2
import numpy as np

def detect_faces(image):

    # Create a face detector
    face_detector = dlib.get_frontal_face_detector()

    # Run detector and get bounding boxes of the faces on image.
    detected_faces = face_detector(image, 1)
    face_frames = [(x.left(), x.top(),
                    x.right(), x.bottom()) for x in detected_faces]

    return face_frames

# Load image
def img_to_pass(path):
    image = io.imread(img_path)

# Detect faces
    detected_faces = detect_faces(image)

# Crop faces and plot
    for n, face_rect in enumerate(detected_faces):
        face = Image.fromarray(image).crop(face_rect)
        print(type(face))
        a=np.array(face)
        cv2.imwrite('image'+str(n+1)+'.png',a)
    
