# dict- data structures
# * key-value - collection (associative array)
# * unordered
# * unique keys
# data atom/ entity

book = {
    # key    : value
    'title'  : 'Python Programming Basics',
    'year'   : 2020,
    'author' : 'Jon Doe'
}
print(book)
print('The book:', book['title'])
print('Published on:', book['year'])
print('Authored by:', book['author'])

if book['year'] >- 2020:
    print('This book is fresh!')
else:
    print('This book is not fresh!')