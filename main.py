from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Bookshelf.db'
db = SQLAlchemy(app)

class Shelf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Shelf %r>' % self.username

# db.create_all()

@app.route('/')
def home():
    all_books = db.session.query(Shelf).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        new = Shelf(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    if request.method == "POST":
        selected = request.form['book_id']
        new_update = Shelf.query.get(selected)
        new_update.rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Shelf.query.get(book_id)
    return render_template('edit.html', for_edit=book_selected)

if __name__ == "__main__":
    app.run(debug=True)

