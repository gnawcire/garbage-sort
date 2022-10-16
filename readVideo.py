from email.mime import image
import cv2 as cv
import os
from flask import Flask, render_template, request, Response, jsonify
from VisionAPI import *

print(os.getcwd())


counter = int
counter = 0


#Reading videos

#takes in path to a video, or integer values, integer like 0, 1, 2, 3 if ur using webcam, most cases it is 0 for the first camera
capture = cv.VideoCapture(0)

app = Flask(__name__)

def generate_frames():
    while True:
        success, frame = capture.read()
        
        cv.imwrite('Images\image' + str(counter) + '.jpg', frame)
        if not success:
            break
        else:
            ret, buffer = cv.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')




@app.route('/background_process_test', methods = ['POST', 'GET'])
def background_process_test():
    whatDo = getLabelList()
    print(whatDo)
    print("hello")
    return whatDo


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/game')
def game():
    return render_template('game.html')

if __name__ =="__main__":
    app.run(debug=True)

