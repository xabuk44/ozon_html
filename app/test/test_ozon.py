from app.ozon import create_book, add_book, search_book, search_book_by_id, remove_book_by_id, create_empty_book


# def test_create_book():
#     data = {'title': 'War and piece', 'author': 'Nikolay Tolstoy', 'tag': 'classic, love, roman'}
#     data.setdefault('id')
#     test = create_book(data['title'], data['author'], data['tag'])
#     test['id'] = None
#     assert test == data

# def test_add_book():
#     container = []
#     data = {'title': 'War and piece', 'author': 'Nikolay Tolstoy', 'tag': 'classic, love, roman'}
#     container = add_book(container, data)
#     assert container == [data]

# def test_search_book():
#     data = {'title': 'War and piece', 'author': 'Nikolay Tolstoy', 'tag': 'classic, love, roman'}
#     data_2 = create_book('Return from the stars', 'Stanislav Lem', 'classic, future, anti utopia')
#     container = [data, data_2]
#     search_result_1 = search_book(container, 'love')
#     search_result_2 = search_book(container, 'tolstoy')
#     search_result_3 = search_book(container, 'war')
#     search_needed = [data_2]
#     assert search_result_1 == search_needed
#     assert search_result_2 == search_needed
#     assert search_result_3 == search_needed


# def test_search_book_by_id():
#     data_1 = create_book('War and piece', 'Nikolay Tolstoy', 'classic, love, roman')
#     data_2 = create_book('Return from the stars', 'Stanislav Lem', 'classic, future, anti utopia')
#     container = [data_1, data_2]
#     id_1 = data_1['id']
#     search = search_book_by_id(container, id_1)
#     assert search == data_1

#
# def test_remove_book_by_id():
#     data_1 = create_book('War and piece', 'Nikolay Tolstoy', 'classic, love, roman')
#     data_2 = create_book('Return from the stars', 'Stanislav Lem', 'classic, future, anti utopia')
#     id_1 = data_1['id']
#     container = [data_1, data_2]
#     container_with_removed_book = [data_2]
#     container = remove_book_by_id(container, id_1)
#     assert container == container_with_removed_book


# def test_create_empty_book():
#     data = {'id': 'new', 'title': '', 'author': '', 'tag': ''}
#     test_data = create_empty_book()
#     assert data == test_data