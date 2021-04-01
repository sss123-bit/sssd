from flask import Flask, render_template, send_from_directory, Response
from errosion import get_string
from id_main import IDCamera
import os
from PIL import Image
import numpy as np
import io
from flask import Flask, render_template, send_from_directory, Response
from pathlib import Path
from capture_id import captureid_and_save
from PIL import Image
import numpy as np
import io
from id_main import IDCamera
import os
app = Flask(__name__)
idc = IDCamera()
x=''
 
ss=os.getcwd()
print(ss)
@app.route('/hh')
def index():
    
    return render_template('index.html', list_header='Deatails',elements=get_details())

def get_details():
    data = get_string(ss+'\last.png')
    return data

@app.route("/")
def entrypoint():
	
	return render_template("sc.html")
def gen(idc):
	
	while True:
		frame = idc.get_frame()
		yield (b'--frame\r\n'
			   b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')

@app.route("/video_feed")
def video_feed():
	return Response(gen(idc),
		mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/rid")
def captureit():
	im = idc.get_frame()
	ss=Image.open(io.BytesIO(im))
	image=np.array(ss)
	x=captureid_and_save(image)
	return index()

if __name__=="__main__":
        app.run(host='localhost',port=5000,use_reloader=False,debug=True)


