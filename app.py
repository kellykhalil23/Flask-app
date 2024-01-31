from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import os



# Get the base directory of the application
base_dir = os.path.abspath(os.path.dirname(__file__))

db_path = os.path.join(base_dir, "DB", "database.db")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
db = SQLAlchemy(app)
fake = Faker()

app.secret_key = 'secret_key'

class Users(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Firstname = db.Column(db.String(50), nullable=False)
    Lastname = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)
    Role = db.Column(db.String(50), nullable=False, default='user')  


@app.route('/')
def index():
    users = Users.query.all()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        First_name = request.form['firstname']
        Last_name = request.form['lastname']
        Email = request.form['email']
        

        new_user = Users(Firstname=First_name, Lastname=Last_name, Email=Email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('add_user.html')


if __name__ == '__main__':
    app.run(debug=True)
