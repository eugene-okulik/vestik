class Book:
    paper_material = 'бумага'
    text = True

    def __init__(self, title, author, pages_quantity, ISBN, reserved):
        self.title = title
        self.author = author
        self.pages_quantity = pages_quantity
        self.ISBN = ISBN
        self.reserved = reserved


class SubjectBook(Book):
    def __init__(self, title, author, pages_quantity, ISBN, reserved, subject, school_class, tasks):
        super().__init__(title, author, pages_quantity, ISBN, reserved)
        self.subject = subject
        self.school_class = school_class
        self.tasks = tasks


book_1 = Book('Идиот', 'Достоевский', 500, 35, True)
book_2 = Book('Земноморье', 'Ле Гуин', 456, 11, False)
book_3 = Book('Снеговик', 'Несбё', 350, 25, False)
book_4 = Book('Бесы', 'Достоевский', 700, 67, False)
book_5 = Book('Pretty Girls', 'Slaughter', 410, 78, False)

books = [book_1, book_2, book_3, book_4, book_5]

for book in books:
    if book.reserved:
        print(
            f'Название: {book.title}, Автор: {book.author},',
            f'страниц: {book.pages_quantity}, материал: {book.paper_material},',
            'зарезервирована'
        )
    else:
        print(
            f'Название: {book.title}, Автор: {book.author},',
            f'страниц: {book.pages_quantity}, материал: {book.paper_material}'
        )

print()

subject_book_1 = SubjectBook('Алгебра', 'Иванов', 350, 65, True,
                             'Математика', 9, True)
subject_book_2 = SubjectBook('География', 'Петров', 216, 111, False,
                             'География', 5, False)
subject_book_3 = SubjectBook('Химия', 'Яковлев', 343, 15, False,
                             'Химия', 10, True)
subject_book_4 = SubjectBook('Английский', 'Попов', 210, 47, True,
                             'Иностранный язык', 2, True)
subject_book_5 = SubjectBook('Литература', 'Королёв', 310, 28, False,
                             'Литература', 7, False)

subject_books = [subject_book_1, subject_book_2, subject_book_3, subject_book_4, subject_book_5]

for book in subject_books:
    if book.reserved:
        print(
            f'Название: {book.title}, Автор: {book.author},',
            f'страниц: {book.pages_quantity}, предмет: {book.subject},',
            f'класс: {book.school_class}, зарезервирована'
        )
    else:
        print(
            f'Название: {book.title}, Автор: {book.author},',
            f'страниц: {book.pages_quantity}, предмет: {book.subject},',
            f'класс: {book.school_class}'
        )
