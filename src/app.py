"""
    main driver 
"""


from flask import Flask,render_template, url_for
from views.auth import users_bp
from models import db
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Configure the application
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db.init_app(app)

# Register blueprints with the applications
app.register_blueprint(users_bp)
@app.route('/')
def index():
    return render_template('index.html')
# Start the application

@app.route('/signup')
def signup():
    return render_template('signup.html')
if __name__ == "__main__":
    app.run(debug=True)
