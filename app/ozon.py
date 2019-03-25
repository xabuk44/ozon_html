import uuid


def create_book(title, author, tag):
    return {
        'id': str(uuid.uuid4()),
        'title': title,
        'author': author,
        'tag': tag
    }


def add_book(container, book):
    copy = container[:]
    copy.append(book)
    return copy


def search_book(container, search):
    result = []
    # for book in container:
    #     if book['title'] == search:
    #         result.append(book)
    #     if book['author'] == search:
    #             result.append(book)
    # return result
    if search:
        search_lowercased = search.strip().lower()
        for book in container:
            if search_lowercased in book['title'].lower():
                result.append(book)
            if search_lowercased in book['author'].lower():
                result.append(book)
            if search_lowercased in book['tag'].lower():
                result.append(book)
    return result

def search_book_by_id(container, book_id):
    for book in container:
        if book['id'] == book_id:
            return book


def remove_book_by_id(container, book_id):
    result = []
    for book in container:
        if book['id'] != book_id:
            result.append(book)
    return result


def create_empty_book():
    return {
        'id': 'new',
        'title': '',
        'author': '',
        'tag': ''

    }

#cделать сохроанения изменения - выложить на хироку
