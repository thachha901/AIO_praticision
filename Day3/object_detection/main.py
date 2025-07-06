import streamlit as st 
import numpy as np
import cv2
from PIL import Image

model = "./model/MobileNetSSD_deploy.caffemodel"
prototxt = "./model/MobileNetSSD_deploy.prototxt.txt"

def process_image(image):
    blob = cv2.dnn.blobFromImage(
        cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5
    )
    
    net =cv2.dnn.readNetFromCaffe(prototxt, model)
    net.setInput(blob)
    detections = net.forward()
    
    return detections

def annotated_image(image, detections, confidence_threshold = 0.5):
    h, w = image.shape[:2]
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > confidence_threshold:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            
            (startX, startY, endX, endY) = box.astype('int')
            
            label = f"Object: {idx} Confidence] {confidence:.2f}"
            cv2.rectangle(image, (startX, startY), (endX, endY), 70, 2)
            cv2.putText(image, label, (startX, startY - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            
    return image



if __name__ == "__main__":
    st.title('Object Detection')
    file = st.file_uploader('Upload an image', type = ['jpg', 'jpeg', 'png'])
    
    if file is not None:
        image = Image.open(file)
        st.image(image)
        image = np.array(image)
        
        detections = process_image(image)
        
        final = annotated_image(image, detections)
        st.image(final, caption = 'Detected Objects')