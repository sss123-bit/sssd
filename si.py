import cv2
def crop_face(path):
# Read the input image
    img = cv2.imread(path)
  
# Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
  

    face_rects=face_cascade.detectMultiScale(face_img,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30)) 
    for (x, y, w, h) in face_rects:
        x = x - 25
        y = y - 40
        roi_color = img[y-5:y + h + 70, x:x + w+50]
        print("[INFO] Object found. Saving locally.")
        cv2.imwrite('face_cropped.png', roi_color)

