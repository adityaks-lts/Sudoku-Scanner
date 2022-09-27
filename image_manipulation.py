import numpy as np
import cv2


if __name__ == "__main__":
    import matplotlib.pyplot as mp

    file = "C:/Users/Animesh/my_data/python/college_project/Sudoku-Scanner/img_1.png"
    img = np.array(cv2.resize(cv2.imread(file,cv2.IMREAD_GRAYSCALE),(450,450),interpolation=cv2.INTER_NEAREST))//255
    upscale_img = cv2.resize(img[4:45,4:45],(100,100),interpolation=cv2.INTER_NEAREST)
    mp.matshow(img[4:45,4:45],cmap='gray')
    mp.matshow(upscale_img,cmap='gray')
    mp.show()