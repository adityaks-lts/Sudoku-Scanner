from pygame import transform, image, Rect
from tkinter.filedialog import askopenfile
from os import getcwd
from keras.models import load_model
from numpy import mat, uint8, argmax
from math import ceil, sqrt
import cv2

class image_section():
    def __init__(self,win,x,y,width,height):
        self.win = win
        self.rect = Rect(x,y,width,height)
        self.image = None
        self.image_surface = None
        self.digit_dict = None
        self.file_types = [("png",".png"),("jpeg",[".jpeg",".jpg"])]
        print("loading model.....")
        self.ocr_model = load_model("basic_model")
        print("model loaded preceeding !!")
    
    def grab_image(self):
        if temp := askopenfile('rb',defaultextension = '.png',filetypes = self.file_types,initialdir=getcwd(),title="select image file "):
            self.image = temp.name
            self.image_surface = transform.smoothscale(image.load(self.image).convert_alpha(),(450,450))

    def process_image(self,image):
        contours ,_ = cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        image = image/255
        for contour in contours:
            x,y,w,h = cv2.boundingRect(contour)
            if int(sqrt((w)**2+(h)**2)) in range(30,50):
                x_off = 30-w;y_off = 30-h
                x-=ceil(x_off/2);y-=ceil(y_off/2);w+=x_off;h+=y_off
                tst_img = image[y:y+h,x:x+w].reshape((1,900))
                txt = argmax(self.ocr_model.predict(tst_img))
                self.digit_dict[y//50][x//50] = {'value':txt,'lock':True}

    def feed_image(self):
        self.digit_dict = {i:{j:{'value':0,"lock":False} for j in range(9)} for i in range(9)}
        img_mat = cv2.imread(self.image,cv2.IMREAD_GRAYSCALE)
        _, img = cv2.threshold(img_mat,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours,key=cv2.contourArea,reverse=True)
        x,y,w,h = cv2.boundingRect(contours[1])
        if w > 200 and h > 200: img_mat = img_mat[y:y+h,x:x+w]
        img_mat = cv2.resize(img_mat,(450,450))
        _, img_mat = cv2.threshold(img_mat,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
        img_mat = cv2.erode(img_mat,mat([[0,1,0],[1,1,1],[0,1,0]],dtype=uint8),iterations=1)
        self.process_image(img_mat)

    def draw(self):
        if self.image: self.win.blit(self.image_surface,self.rect)

    def run(self):
        self.draw()