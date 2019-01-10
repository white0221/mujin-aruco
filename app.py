import cv2
import base64

from flask import Flask, jsonify, make_response
from src import Camera, ArUco, ndarray_ids_to_list


CAMERA_PORT = 0

app = Flask(__name__)
cam = Camera(CAMERA_PORT)
arc = ArUco()

@app.route('/items')
def main():
    img = cam.capturing()
    _, ids, _ = arc.detecting(img)

    response = {'ids': None, 'error': None}
    if ids is None:
        response['error'] = 'cannot detect aruco marker'
    else:
        ids = ndarray_ids_to_list(ids)
        response['ids'] = ids

    response = make_response(jsonify(response))
    response.mimetype = 'application/json'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
