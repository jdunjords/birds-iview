from flask import Flask, jsonify, render_template, request, redirect, url_for
import os
from flask_cors import CORS
UPLOAD_FOLDER = './static/uploads/'
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg'])

############ INITIALIZATION ##############################
# initialize app
app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

# configuration
DEBUG = True

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

######### ROUTES ########################################
# route to home
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title= 'Home')

# route to about
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title= 'About')

# # route to blog
# @app.route('/blog', methods=['GET'])
# def blog():
#     return render_template('blog.html', title= 'Blog')

# route to forum
@app.route('/forum', methods=['GET'])
def forum():
    return render_template('forum.html', title= 'Forum')

# route to learn
@app.route('/learn', methods=['GET'])
def learn():
    return render_template('learn.html', title= 'Learn')

# route to mypeep
@app.route('/mypeep', methods=['GET'])
def mypeep():
    return render_template('mypeep.html', title= 'My Peep')

# route to signup
@app.route('/signup', methods=['GET', 'POST'])
def signup(): 
    if request.method == "POST":
        # get input values from sign up form
        first_name = request.form["inputFirstName"]
        last_name = request.form["inputLastName"]
        user_email = request.form["inputEmail"]
        user_password =  request.form["inputPassword"]
        confirmed_password = request.form["confirmedPassword"]

        # an array of the user information
        user = [first_name, last_name, user_email,
         user_password, confirmed_password]

        # printing out the user information
        for info in user:
            print(info)
    return render_template('signup.html', title= 'Sign Up')

# # route to science
# @app.route('/science', methods=['GET'])
# def science():
#     return render_template('science.html', title= 'Science')

# # route to store
# @app.route('/store', methods=['GET'])
# def store():
#     return render_template('store.html', title= 'Store')

# allowed file name
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# upload an image
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\', '/'))
            return  '{"filename":"%s"}' % filename

if __name__ == '__main__':
    app.run()