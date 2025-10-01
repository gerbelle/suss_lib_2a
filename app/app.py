from flask import Flask, request, render_template
from .books import all_books

app = Flask(__name__)

@app.route('/')
@app.route('/book_titles')
def book_titles():
    # sort alphabetically by title
    sorted_books = sorted(all_books, key=lambda b: b['title'].lower())
    return render_template('book_titles.html', books=sorted_books)