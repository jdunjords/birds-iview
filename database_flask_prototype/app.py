from flask import Flask, render_template, request, redirect, jsonify
from flask.helpers import make_response, url_for
from flask_cors import CORS
from flask_mysqldb import MySQL
import yaml
import os

app = Flask(__name__,
			template_folder="templates",
			static_folder="static")

# get database connection info
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

# delcare our upload folder dest and allowable img extensions
UPLOAD_FOLDER = './static/uploads/'
ALLOWED_EXTENSIONS = set(['jpg','png'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 #TODO what do these dimensions refer to

# configure cross-origin resource sharing TODO research this
CORS(app)

# connect to the database
mysql = MySQL(app)

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/create-account', methods =['GET', 'POST'])
def create_account(): 
	if request.method == 'POST':
		#Fetch form data
		user_details = request.form 
		name = user_details['name']
		email = user_details['email']
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO user(name, email) VALUES(%s, %s)",(name, email))
		mysql.connection.commit()
		cur.close()
		return make_response('Account created', 200)

@app.route('/upload-image', methods=['GET', 'POST'])
def upload_image():
	file = request.files['file']
	if file.filename != '':
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename).replace('\\','/'))
	return redirect(url_for('index'))

'''
A helper function to validate file extensions for incoming file
'''
def allowed_file(filename):
	return '.' in filename and \
			filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
	app.run(debug=True) 

