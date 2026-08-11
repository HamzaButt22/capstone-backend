import cv2

def analyze_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Could not read image at {image_path}")

    xml_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(xml_path)
    if face_cascade.empty():
        raise RuntimeError(f"Failed to load cascade classifier from {xml_path}")

    resized_image = cv2.resize(image, (500, 500))
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    return {"face_detected": len(faces) > 0, "count": len(faces)}