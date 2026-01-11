import tkinter as tk
import cv2
from keras.models import load_model
from PIL import Image, ImageTk
import numpy as np
import sys
import subprocess


class CameraApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.window.geometry('375x667')
        self.window.configure(bg="pink")
        self.video_source = 0
        self.vid = cv2.VideoCapture(self.video_source)
        
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        
        self.bt_snapshot = tk.Button(self.window, text="Snap", width=10, command=self.snapshot, bg='#EFB0F4',font=("Helvetica", 10))
        self.bt_snapshot.place(x=150,y=600)

        self.new = tk.Button(window, text="New", width=10, command=self.reset,bg='#EFB0F4',font=("Helvetica", 10))
        self.new.place(x=280,y=600)

        self.rt_button= tk.Button(window, text="Back", width=10, command=self.run_menu,bg='#EFB0F4',font=("Helvetica", 10))
        self.rt_button.place(x=10,y=600)

        self.model = load_model("keras_Model.h5")
        self.labels = open("labels.txt", "r").readlines()

        self.update()
        
        self.window.mainloop()
        
    def run_menu(self):
        self.window.destroy() 
        self.window.after(1000,subprocess.call([sys.executable, 'C:\\Users\\ADMIN\\OneDrive\\Desktop\\tkinter\\build\\gui_menu.py']))

    def snapshot(self):
        ret, frame = self.vid.read()
        if ret:
            cv2.imwrite("C:/Users/ADMIN/OneDrive/Desktop/tkinter/present_pic/snapshot.png", frame)
            print("Ảnh đã được lưu thành công!")
            
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (224, 224))
            img = np.expand_dims(img, axis=0)
            img = img / 255.0  
            prediction = self.model.predict(img)
            label_index = np.argmax(prediction)
            label = self.labels[label_index]
            
            self.lb = tk.Label(self.window,
                               text=f"Food: {label[2:]}",
                               width=20,
                               font=("Helvetica", 20),
                               bg='pink',
                               fg='red')
            self.lb.place(x=30,y=500)

            self.vid.release()
            self.photo = tk.PhotoImage(file="C:/Users/ADMIN/OneDrive/Desktop/tkinter/present_pic/snapshot.png")
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        else:
            print("Không thể chụp ảnh!")

    def reset(self):
        self.vid = cv2.VideoCapture(self.video_source)
        self.canvas.delete("all")
        self.lb.destroy()
        self.update()
        
    def update(self):
        ret, frame = self.vid.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(10, self.update)


    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

CameraApp(tk.Tk(), "Camera App")
