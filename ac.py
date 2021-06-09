import sys
import os
import dlib
import glob
faces_folder_path="C:/Users/Administrator/Desktop/caffemodel/"
# Load all the models we need: a detector to find the faces, a shape predictor
# to find face landmarks so we can precisely localize the face, and finally the
# face recognition model.
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor('C:/Users/Administrator/Desktop/caffemodel/shape_predictor_5_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('C:/Users/Administrator/Desktop/caffemodel/dlib_face_recognition_resnet_model_v1.dat')

win = dlib.image_window()

# Now process all the images
for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
    print("Processing file: {}".format(f))
    img = dlib.load_rgb_image(f)

    win.clear_overlay()
    win.set_image(img)

    # Ask the detector to find the bounding boxes of each face. The 1 in the
    # second argument indicates that we should upsample the image 1 time. This
    # will make everything bigger and allow us to detect more faces.
    dets = detector(img, 1)
    print("Number of faces detected: {}".format(len(dets)))

