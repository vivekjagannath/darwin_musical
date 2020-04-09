import sounddevice as sd
import numpy as np
import cv2
import time
from datetime import datetime
camera = cv2.VideoCapture(2)
starttime = time.time()
global count
count = 0
duration = 10 
def print_sound(indata, outdata, frames, t, status):
	
	volume_norm = np.linalg.norm(indata)*10
	loudness = int(volume_norm)
	return_value, image = camera.read()
	if loudness > 60:
		global count
		count = count+1
		cv2.imwrite(str(count)+'.png', image)
		print(loudness)
		print("heard")
		print(str(count)+'.png')
		time.sleep(1)
		return
with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)
