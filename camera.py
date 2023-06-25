# pip install opencv-python
import cv2


class Camera:

    def __init__(self, id_cam, width, height) -> None:
        self.camera = cv2.VideoCapture()
        # Ustaw rozmiar okna kamery
        self.camera.open(id_cam)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        if not self.camera.isOpened():
            raise ValueError("Unable to open Camera.")
        
        self.width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        
    def __del__(self) -> None:
        if self.camera.isOpened():
            self.camera.release()

    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            else:
                return (ret, None)
        else:
            return None