import tkinter as tk
from tkinter import simpledialog
import cv2
import os
# pip install pillow
import PIL.Image, PIL.ImageTk
import camera

class App:

    def __init__(self, window=tk.Tk(), window_tittle="Camera View") -> None:
        self.window = window
        self.window_tittle = window_tittle

        self.cameras = []
        # self.camera_one = camera.Camera(1, 640, 480)
        # self.camera_two = camera.Camera(2, 640, 480)

        num_cameras = 5
        for i in range(num_cameras):
            # Sprawdzenie, czy kamera jest dostępna
            available, _ = cv2.VideoCapture(i).read()
            if available:
                self.cameras.append(camera.Camera(i, 640, 480))
            else:
                print(f"Kamera {i}: Niedostępna")
        print("init")
        print(self.cameras)

        self.init_gui()

        self.delay = 10
        self.update()

        self.window.attributes('-topmost', True)
        self.window.mainloop()

    def init_gui(self):
        self.canvas = []

        for index, camera in enumerate(self.cameras):
            canva = tk.Canvas(self.window, width=self.cameras[index].width, height=self.cameras[index].height)
            canva.grid(row=0, column=index)
            self.canvas.append(canva)
        print("init_gui")
        print(self.canvas)

        # self.canvas = tk.Canvas(self.window, width=self.camera_one.width, height=self.camera_one.height)
        # self.canvas.pack()
        # self.canvas2 = tk.Canvas(self.window, width=self.camera_two.width, height=self.camera_two.height)
        # self.canvas2.pack()
        # self.canvas0 = tk.Canvas(self.window, width=self.camera_zero.width, height=self.camera_zero.height)
        # self.canvas0.pack()


    # fixed update
    def update(self):
        # print("update")
        self.photos = []

        for index, _ in enumerate(self.cameras):
            # print(index)
            self.photos.append(None)

        for index, _ in enumerate(self.cameras):
            # print(index)
            ret, frame = self.cameras[index].get_frame()
            if ret:
                self.photos[index] = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
                self.canvas[index].create_image(0, 0, image=self.photos[index], anchor=tk.NW)


        # ret, frame = self.cameras[0].get_frame()
        # ret1, frame1 = self.cameras[1].get_frame()

        # if ret:
        #     self.photos[0] = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        #     self.canvas[0].create_image(0, 0, image=self.photos[0], anchor=tk.NW)
        
        # if ret1:
        #     self.photos[1] = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame1))
        #     self.canvas[1].create_image(0, 0, image=self.photos[1], anchor=tk.NW)

        # ret, frame = self.camera_one.get_frame()
        # ret2, frame2 = self.camera_two.get_frame()
        # ret0, frame0 = self.camera_zero.get_frame()

        # if ret:
        #     self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        #     self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        # if ret2:
        #     self.photo2 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame2))
        #     self.canvas2.create_image(0, 0, image=self.photo2, anchor=tk.NW)
        # if ret0:
        #     self.photo0 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame0))
        #     self.canvas0.create_image(0, 0, image=self.photo0, anchor=tk.NW)

        self.window.after(self.delay, self.update)