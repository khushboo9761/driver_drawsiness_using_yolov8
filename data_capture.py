from datetime import datetime
import time
import cv2
import tkinter as tk
from tkinter import Button, Label
from PIL import Image, ImageTk

class CaptureCameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reproductor de Cámara")

        self.cap = cv2.VideoCapture(0)
        time.sleep(1.000)
        self.label = Label(root)
        self.label.grid(column=0,row=3, columnspan=3)

        self.btn_yawn = Button(root, text="Captura para Bostezo", command=lambda: self.capture_action_image("yawn"))
        self.btn_yawn.grid(column=0,row=0,padx=5,pady=5)

        self.btn_drowsy = Button(root, text="Captura para Ojos cerrados",command=lambda: self.capture_action_image("drowsy"))
        self.btn_drowsy.grid(column=1,row=0,padx=5,pady=5)

        self.btn_awake = Button(root, text="Captura para Despierto", command=lambda: self.capture_action_image("awake"))
        self.btn_awake.grid(column=2,row=0,padx=5,pady=5)

        self.lblinfo = Label(root,text="Video de Entrada: ")
        self.lblinfo.grid(column=1,row=1,rowspan=1)

        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)
            self.label.after(10, self.update_frame)
        else:
            self.cap.release()

    def capture_action_image(self, action):
        print("entra")
        ret, frame = self.cap.read()
        if ret:
            dateid = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            cv2.imwrite("dataset/{}_{}.jpg".format(action, dateid), frame)
            print("Imagen capturada y guardada como '{}/data_{}.jpg'".format(action, dateid))


# Crear la ventana de Tkinter
root = tk.Tk()
app = CaptureCameraApp(root)
root.mainloop()
