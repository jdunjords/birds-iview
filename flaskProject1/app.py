from flask import Flask,render_template,request,redirect,jsonify
import os
from flask_cors import CORS
UPLOAD_FOLDER = './static/uploads/'  #the path of files
ALLOWED_EXTENSIONS = set(['jpg','png','pdf']) #Limits upload file formats
BASE_DIR = 'D:\\flaskProject1\\'
app = Flask(__name__,template_folder="templates",static_folder="static")
CORS(app)#Cross-Origin Resource Sharing
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
print(BASE_DIR)
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
            return jsonify({'data':'Upload Success！'})
@app.route('/show_pic/', methods=['GET', 'POST'])
def show_file():
    list_pics = os.listdir(os.path.join(BASE_DIR,'static','uploads'))
    list_all = []
    for i in list_pics:
        list_all.append('/static/uploads/'+i)
    return jsonify({'data':list_all})
if __name__ == '__main__':
    app.run(debug=True)
