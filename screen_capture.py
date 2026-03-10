import cv2
from PIL import ImageGrab
import numpy as np
from screeninfo import get_monitors

for m in get_monitors():
    print(m)
    if m.is_primary:
        x : int = m.x
        y : int = m.y
        width : int = m.width
        height : int = m.height

# video encoding
fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
captured_video = cv2.VideoWriter("recorded_video.mp4",fourcc,10.0,(width,height))

while True:
    img = ImageGrab.grab(bbox=(x,y,width,height)) 

    np_img = np.array(img)

    cvt_img = cv2.cvtColor(np_img,cv2.COLOR_BGR2RGB)
    cv2.imshow("video capture", cvt_img)

    captured_video.write(cvt_img)

    # lets us quit
    key = cv2.waitKey(20) 
    if key == 27:
        break

cv2.destroyAllWindows()
    
# another test