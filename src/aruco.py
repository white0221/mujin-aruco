import cv2


aruco = cv2.aruco

class ArUco(object):
    def __init__(self):
        # 4x4の0-1000のIDを生成可能
        self.aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_1000)

    def generating(self, _id, side_pixel=64):
        return aruco.drawMarker(self.aruco_dict, _id, side_pixel)

    def restoring(self, filename, marker):
        cv2.imwrite(filename, marker)

    def detecting(self, image):
        corners, ids, rejectedImgPoints = aruco.detectMarkers(image, self.aruco_dict)
        return [corners, ids, rejectedImgPoints]
