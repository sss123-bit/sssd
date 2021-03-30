from flask import Flask, render_template, send_from_directory, Response
import re
app = Flask(__name__)
@app.route('/')
def index():
    
    return render_template('ggg.html')
@app.route('/hh', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        x=request.get_json()
        img=x['base64']
        print(img)
    
if __name__=="__main__":
        app.run(host='localhost',port=5000,use_reloader=False,debug=True)


