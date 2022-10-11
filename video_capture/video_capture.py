import cv2
import os
import logging

class ExeVideoCapture:
    
    def __init__():
        pass
    
    def get():
        pass




path = ''
file_path = os.path.join(path, '')

try:
    cap = cv2.VideoCapture(file_path)
except Exception as e:
    logging.exception(e)
    exit()
    
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_size = (frame_width, frame_height)
print(f'frame_size={frame_size}')

frameRate = 33

while True:
    
    retval, frame = cap.read()
    print(f'retval type: {type(retval)}')
    print(f'frame type {type(frame)}')
    
    if not(retval):
        break
    
    cv2.imshow('frame', frame)
    key = cv2.waitKey(frameRate)  # frameRate msec 동안 한 프레임을 보여준다.
    
    if key == 27:
        break
    
if cap.isOpened():
    cap.release()
    
cv2.destroyAllWindows()