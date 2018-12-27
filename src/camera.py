import cv2


class Camera(object):
    def __init__(self, port):
        self.capture = cv2.VideoCapture(port)

    def capturing(self):
        ret, img = self.capture.read()
        return img
