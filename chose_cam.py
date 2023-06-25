import tkinter as tk
from tkinter import simpledialog
import cv2
import os
# pip install pillow
import PIL.Image, PIL.ImageTk
import camera


class App:
    def __init__(self, window=tk.Tk(), window_title="Camera View"):
        self.window = window
        self.window.title(window_title)
        self.cameras = []
        self.selected_camera_index = 0  # Indeks wybranej kamery

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
        self.create_menu()

        self.delay = 10
        self.update()

        self.window.attributes('-topmost', True)
        self.window.mainloop()

    def init_gui(self):
        self.canvas = []
        for index, _ in enumerate(self.cameras):
            canvas = tk.Canvas(self.window, width=self.cameras[index].width, height=self.cameras[index].height)
            canvas.grid(row=0, column=index)
            self.canvas.append(canvas)
        print("init_gui")
        print(self.canvas)

    def create_menu(self):
        menu_bar = tk.Menu(self.window)
        self.window.config(menu=menu_bar)

        camera_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Kamera", menu=camera_menu)

        for index, _ in enumerate(self.cameras):
            camera_menu.add_command(label=f"Kamera {index}", command=lambda idx=index: self.change_camera(idx))

    def change_camera(self, index):
        self.selected_camera_index = index

    def update(self):
        self.photos = []
        for index, _ in enumerate(self.cameras):
            self.photos.append(None)

        # for index, _ in enumerate(self.cameras):
        #     ret, frame = self.cameras[index].get_frame()
        #     if ret:
        #         self.photos[index] = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        #         self.canvas[index].create_image(0, 0, image=self.photos[index], anchor=tk.NW)

        ret, frame = self.cameras[self.selected_camera_index].get_frame()
        if ret:
            self.photos[0] = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas[0].create_image(0, 0, image=self.photos[0], anchor=tk.NW)

        self.window.after(self.delay, self.update)


app = App()