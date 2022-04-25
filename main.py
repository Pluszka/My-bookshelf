from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    library = True
    if len(all_books) < 1:
        library = False
    return render_template('index.html', books=all_books, length=library)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        new = {
            'title': request.form['title'],
            'author': request.form['author'],
            'rating': request.form['rating']
        }
        all_books.append(new)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

