from flask import Flask,render_template,request,redirect,jsonify
import os
from flask_cors import CORS
UPLOAD_FOLDER = './static/uploads/'  #文件存放路径
ALLOWED_EXTENSIONS = set(['jpg','png']) #限制上传文件格式

app = Flask(__name__,template_folder="templates",static_folder="static")
CORS(app)#跨域
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\','/'))
            return  '{"filename":"%s"}' % filename


if __name__ == '__main__':
    app.run(debug=True)    