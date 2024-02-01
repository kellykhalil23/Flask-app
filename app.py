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

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)
   


@app.route('/books')
def index():
    books = Book.query.all()
    return render_template('books.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        publication_year = request.form['publication_year']
        author = request.form['author']
    

        new_book = Book(title=title, author=author, publication_year=publication_year)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('book_list'))

    return render_template('add_book.html')


if __name__ == '__main__':
    app.run(debug=True)
