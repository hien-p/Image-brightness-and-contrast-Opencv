import numpy as np
import cv2 as cv
import cv2


cap = cv.VideoCapture(0)

if (cap.isOpened() == False):
    print("Error opening video file")

alpha = 1.0 # Simple contrast control
beta = 0    # Simple brightness control


def brightness_images(Frame):
    contrast = 1.25
    brightness = 50

    # Convert Red-Green Blue (RGB) to Hue-Saturation-Value (HSV) first (“Value” is the same as “Brightness”)
    frame = cv2.cvtColor(Frame, cv2.COLOR_BGR2HSV)
    # “Slice” the Numpy array to the Value portion of the Numpy array and adjust brightness and contrast on that slice
    # numpy.clip() ensures that all the pixel values remain between 0 and 255 in each on the channels (R, G, and B). 
    frame[:,:,2] = np.clip(contrast * Frame[:,:,2] + brightness, 0, 255)
    # Convert back from HSV to RGB.
    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    #cv.imshow('brightness_images',frame)
    return frame

def CLAHE(Frame):
    # adaptive histogram equalization 
    image_bw = cv.cvtColor(Frame, cv.COLOR_BGR2GRAY)
    # create a CLAHE object (Arguments are optional).
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    final_img = clahe.apply(image_bw) + 30
    
    return final_img


while cap.isOpened():

    ret, Frame = cap.read()

    if ret == True:
        cv.imshow('image normal:',Frame)
        
        Frame = brightness_images(Frame)
        #cv.imshow('brightness_images',frame)
        # using global histogram equalization
        src = cv.cvtColor(Frame, cv.COLOR_BGR2GRAY)
        dst = cv.equalizeHist(src)
        cv.imshow('Histogram Equalization?', dst)

        # cv.imshow('Image', new_image)
        final_img = CLAHE(Frame)
        cv2.imshow("CLAHE image", final_img)
        
        if cv.waitKey(25) & 0xFF == ord('q'):
            break   
    else:
        break



cap.release()
cv.destroyAllWindows()