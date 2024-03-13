import pyautogui
import cv2
import numpy as np

#Specifying resolution
resolution = (1920, 1080)
#Specifying video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

#Specifying name of the output file
filename = "Recording.avi"
#Specifying frames rate. We can choose
#any value and experiment with it
fps = 60.0
#Creating a VideoWrite object
out = cv2.VideoWriter(filename, codec, fps, resolution)

############-----We have to display the recording in real-time, therefore, creating an empty window and resizing it would be necessary-----############
#Creating an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

#Resizing the window
cv2.resizeWindow("Live", 480, 270)

###########----Now we start recording the screen----#########
while True:
    #Taking screenshot using PyAutoGUI
    img = pyautogui.screenshot()
    #Converting the screenshot to a numpy array
    frame = np.array(img)
    #Converting it from BRG(Blue, Green, Red) to
    #RBG(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #Writing it to the output file
    out.write(frame)
    #optional: Displaying the recording screen
    cv2.imshow('Live', frame)
    #Stop recording when wepress 'q'
    if cv2.waitKey(1) == ord('q'):
        break
########################-----After everything is don, we will release the write and destroy all windows opened by OpenCV.------------#######################
out.release()
#Destroying all windows
cv2.destroyALLWindows()
