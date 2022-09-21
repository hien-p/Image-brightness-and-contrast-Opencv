# Extracthandregion.py

import numpy as np
import cv2 as cv
import cv2

# Initialize the VideoCapture object to read from the webcam.
camera_video = cv2.VideoCapture(0)

# Create a named resizable window.
cv2.namedWindow('Webcam Feed')

# Get the height and width of the frame of the webcam video.
frame_height = int(camera_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_width = int(camera_video.get(cv2.CAP_PROP_FRAME_WIDTH))

# Create the onChange function for the trackbar since its mandatory.
def nothing(x):
    pass

# Create trackbar named Radius with the range [0-100].
cv2.createTrackbar('Radius: ', 'Webcam Feed', 50, 100, nothing) 

# Create trackbar named x with the range [0-frame_width].
cv2.createTrackbar('x: ', 'Webcam Feed', 50, frame_width, nothing) 

# Create trackbar named y with the range [0-frame_height].
cv2.createTrackbar('y: ', 'Webcam Feed', 50, frame_height, nothing) 


cv.createTrackbar('R','Webcam Feed',0,255,nothing)
cv.createTrackbar('G','Webcam Feed',0,255,nothing)
cv.createTrackbar('B','Webcam Feed',0,255,nothing)


# font
font = cv2.FONT_HERSHEY_SIMPLEX
  
# org
org = (50, 50)
  
# fontScale
fontScale = 1
   
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2

# Iterate until the webcam is accessed successfully.
while camera_video.isOpened():
    
    # Read a frame.
    ok, frame = camera_video.read()
    
    # Check if frame is not read properly then continue to the next iteration to read the next frame.
    if not ok:
        continue
    
    # Get the value of the radius of the circle (ball).
    radius = cv2.getTrackbarPos('Radius: ', 'Webcam Feed')
    
    # Get the x-coordinate value of the center of the circle (ball).
    x = cv2.getTrackbarPos('x: ', 'Webcam Feed')
    
    # Get the y-coordinate value of the center of the circle (ball).
    y = cv2.getTrackbarPos('y: ', 'Webcam Feed')
    
    # create trackbars for color change 
    r = cv.getTrackbarPos('R','Webcam Feed')
    g = cv.getTrackbarPos('G','Webcam Feed')
    b = cv.getTrackbarPos('B','Webcam Feed')
    # Draw the circle on the frame.
    cv2.circle(img=frame, center=(x, y),
               radius=radius, color=(b,r,g), thickness=-1)
    
    # Display the frame.
    image = cv2.putText(frame, '520H0631', org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow('Webcam Feed', image)    

    # Check if 'ESC' key is pressed and break the loop.
    if cv.waitKey(25) & 0xFF == ord('q'):
        break
        
# Release the VideoCapture Object and close the windows.
camera_video.release()
cv2.destroyAllWindows()

