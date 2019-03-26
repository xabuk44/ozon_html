import os

import waitress
from flask import Flask, render_template, request, url_for, redirect

from app.ozon import create_book, add_book, search_book, search_book_by_id, remove_book_by_id, create_empty_book



def start():
    app = Flask(__name__)

    container = []
    wp = create_book('War and piece', 'Nikolay Tolstoy', 'classic, love, roman')
    ak = create_book('Return from the stars', 'Stanislav Lem', 'classic, future, anti utopia')

    #сделать распаковку эдд буууук
    container = add_book(container, wp)
    container = add_book(container, ak)

    @app.route('/')
    def index():
        search = request.args.get('search')
        if search:
            results = search_book(container, search)
            return render_template('index.html', books=results, search=search)
        return render_template('index.html', books=container)

    @app.route('/books/<book_id>')
    def book_details(book_id):
        result = search_book_by_id(container, book_id)
        return render_template('book-details.html', book=result)

    @app.route('/books/<book_id>/edit')
    def book_edit(book_id):
        book = None
        if book_id == 'new':
            book = create_empty_book()
        else:
            book = search_book_by_id(container, book_id)
        return render_template('book-edit.html', book=book)
    #при добалвоении - новую пустью хуйню создаем

    @app.route('/books/<book_id>/remove', methods=['POST'])
    def remove_book(book_id):
        nonlocal container
        container = remove_book_by_id(container, book_id)
        return redirect(url_for('index'))

    @app.route('/books/<book_id>/save', methods=['POST'])
    def book_save(book_id):
        nonlocal container
        title = request.form['title']
        author = request.form['author']
        tag = request.form['tag']
        if book_id == 'new':
            book = create_book(title=title, author=author, tag=tag)
            container = add_book(container, book)
        else:
            book = search_book_by_id(container, book_id)
            pass # сохранить изменения TO DO
            return redirect(url_for('book_details', book_id=book['id']))
        return redirect(url_for('index'))
         #урл_фор редиректит на определенню стьагницу - которую прост опишем имя без расширения после точки /html


    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
     app.run(port=9009, debug=True)


if __name__ == '__main__':
    start()
