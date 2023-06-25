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
        num_cameras = 5
        for i in range(num_cameras):
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


    def init_gui(self) -> None:
        self.canvas = []
        for index, _ in enumerate(self.cameras):
            canva = tk.Canvas(self.window, width=self.cameras[index].width, height=self.cameras[index].height)
            canva.grid(row=0, column=index)
            self.canvas.append(canva)
        print("init_gui")
        print(self.canvas)


    def update(self) -> None:
        self.photos = []
        for index, _ in enumerate(self.cameras):
            self.photos.append(None)
        for index, _ in enumerate(self.cameras):
            ret, frame = self.cameras[index].get_frame()
            if ret:
                self.photos[index] = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
                self.canvas[index].create_image(0, 0, image=self.photos[index], anchor=tk.NW)
        self.window.after(self.delay, self.update)