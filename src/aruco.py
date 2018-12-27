import cv2


aruco = cv2.aruco

class ArUco(object):
    def __init__(self, size=4, num_creation=1000):
        aruco_dict_name = 'DICT_{}X{}_{}'.format(size, size, num_creation)
        aruco_dict_id = None
        try:
            aruco_dict_id = getattr(aruco, aruco_dict_name)
        except:
            Exception('invalid aruco dict')

        self.aruco_dict = aruco.getPredefinedDictionary(aruco_dict_id)

    def generating(self, _id, side_pixel=64):
        return aruco.drawMarker(self.aruco_dict, _id, side_pixel)

    def restoring(self, filename, marker):
        cv2.imwrite(filename, marker)

    def detecting(self, image):
        corners, ids, rejectedImgPoints = aruco.detectMarkers(image, self.aruco_dict)
        return [corners, ids, rejectedImgPoints]
