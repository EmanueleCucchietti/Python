import cv2
from PIL import Image, ImageStat
import statistics
import math
import numpy as np
import screen_brightness_control as sbc
  
# define a video capture object
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
nframes = 0
maxNframes = 20
r, g, b = [], [], []
  
while(nframes < maxNframes):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    im_pil = Image.fromarray(frame)
    stat = ImageStat.Stat(im_pil)
    rx,gx,bx = stat.mean
    r.append(rx)
    g.append(gx)
    b.append(bx)
    
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    nframes += 1

# After the loop release the cap object

r = statistics.mean(r)
g = statistics.mean(g)
b = statistics.mean(b)
brightness = math.sqrt(0.299*(r**2) + 0.587*(g**2) + 0.144*(b**2))
print(brightness)


b_level = np.interp(brightness,[15,220],[0,100])
sbc.set_brightness(int(b_level))


  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()