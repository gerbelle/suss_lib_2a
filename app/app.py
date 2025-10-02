from flask import Flask, request, render_template
from .books import all_books

app = Flask(__name__)

def get_unique_categories(books):
    categories = set()
    for book in books:
        if 'category' in book and book['category']:
            categories.add(book['category'])
    return sorted(categories)


def get_book_by_title(book_title):
    """Finds a single book dictionary from all_books by matching the book's 'title'."""
    
    for book in all_books:
        if book.get('title') == book_title:
            return book
    return None 

@app.route('/')
@app.route('/book_titles')
def book_titles():
    # 1. Get the selected category from the request
    selected_category = request.args.get('category', 'All')

    # 2. Start with all books
    books_to_display = all_books

    # 3. Filter the books if a specific category is selected
    if selected_category != 'All':
        books_to_display = [
            book for book in all_books 
            if book.get('category') == selected_category
        ]

   
    sorted_books = sorted(books_to_display, key=lambda b: b['title'].lower())
    unique_categories = get_unique_categories(all_books) 

    return render_template(
        'book_titles.html', 
        books=sorted_books,
        selected_category=selected_category,  
        unique_categories=unique_categories 
    )

    # # sort alphabetically by title
    # sorted_books = sorted(all_books, key=lambda b: b['title'].lower())
    # return render_template('book_titles.html', books=sorted_books)

@app.route('/book/<string:book_title>')
def book_detail(book_title):
    book = get_book_by_title(book_title)

    if book is None:
        return "Book not found", 404

    # 3. Render the template
    return render_template('book_detail.html', book=book)