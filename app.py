import cv2
import base64

from flask import Flask
from src import Camera, ArUco, ndarray_ids_to_list


CAMERA_PORT = 0

app = Flask(__name__)
cam = Camera(CAMERA_PORT)
arc = ArUco()

@app.route('/items')
def main():
    img = cam.capturing()
    _, ids, _ = arc.detecting(img)

    response = None
    if ids == None:
        response = 'cannot detecting aruco marker'
    else:
        ids = ndarray_ids_to_list(ids)
        response = ' '.join([str(id_) for id_ in ids])
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
