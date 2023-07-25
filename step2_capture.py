import os
import shutil
from time import sleep
from PIL import Image
import cv2

from jetcam.csi_camera import CSICamera

#camera = CSICamera(width=224, height=224)
folder_path="./picture"
# Delete the "picture" folder and its contents if it exists
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
    
# Create the "picture" folder
os.mkdir(folder_path)

# Capture and save images continuously
count = 0
while True:
    # Capture an image from the camera
    snapshot = camera.value.copy()
    cv2.imwrite(os.path.join(folder_path, "%08d.jpg" % (count)), snapshot)
    
    # Increment the count
    count += 1
    
    # Wait for 2 seconds
    sleep(0.3)
