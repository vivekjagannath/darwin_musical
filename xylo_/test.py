import sounddevice as sd
import numpy as np
import cv2
import time
from datetime import datetime
camera = cv2.VideoCapture(1)
starttime = time.time()
global count
count = 0
duration = 10 
def print_sound(indata, outdata, frames, time, status):
	
	volume_norm = np.linalg.norm(indata)*10
	loudness = int(volume_norm)
	if loudness > 60:
		print(loudness)
		global count
		count = count+1
        return_value, image = camera.read()		
		cv2.imwrite(str(count)+'.png', image)		
		print(str(count)+'.png')		
with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)