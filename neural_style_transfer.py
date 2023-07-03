import imutils
import cv2
import numpy as np
import logging

def get_model_from_path(style_model_path):
    try:
        model = cv2.dnn.readNetFromTorch(style_model_path)
        return model
    except Exception as e:
        logging.error(f"An error occurred while loading the style model: {str(e)}")
        return None

def style_transfer(image, model):
    try:
        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(image, 1.0, (w, h), (103.939, 116.779, 123.680), swapRB=False, crop=False)
        model.setInput(blob)
        output = model.forward()
        output = output.reshape((3, output.shape[2], output.shape[3]))
        output[0] += 103.939
        output[1] += 116.779
        output[2] += 123.680
        output /= 255.0
        output = output.transpose(1, 2, 0)
        output = np.clip(output, 0.0, 1.0)
        output = imutils.resize(output, width=2160) # Adjust the width to 3840 for 4K resolution
        return output
    except Exception as e:
        logging.error(f"An error occurred during style transfer: {str(e)}")
        return None
