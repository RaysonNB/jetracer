import cv2
import os


def mouse_callback(event, x, y, flags, param):
    global cnt
    cnt+=1
    if event == cv2.EVENT_LBUTTONDOWN:
        #circle(img, (x, y), 5, (0, 0, 255), -1)
        E=img.copy()
        cv2.circle(E, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow("image", E)
        filename = os.path.basename(file_path)
        filename_parts = os.path.splitext(filename)
        new_filename = f"{x}_{y}_" + filename_parts[0]+filename_parts[1]
        print(filename_parts[0], filename_parts[1])
        
        output_path = os.path.join(output_folder, new_filename)
        cv2.imwrite(output_path, img)


folder_path = "C:/Users/dell/Desktop/jetracer/start_picture"

output_folder = "C:/Users/dell/Desktop/jetracer/apex/"

file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]

cnt=0
for file_path in file_paths:
    if file_path.endswith(".jpg"):
        img = cv2.imread(file_path)

        cv2.imshow("image", img)
        cv2.setMouseCallback("image", mouse_callback)
        cv2.waitKey(0)

        cv2.destroyAllWindows()
