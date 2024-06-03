#!/usr/bin/python3

if __name__ == '__main__':
    import uuid
    from models import storage
    from models.user import User
    from models.book import Book
    from models.badge import Badge
    from models.book_reading import BookReading
    from models.book_review import BookReview
    user = User()
    user.add()
    user.save()

    book = Book()
    book.add()
    book.save()

    breview = BookReview(**{'book_id': str(uuid.uuid4()), 'reviewer_id': str(uuid.uuid4())})
    breview.add()
    breview.save()

    br = BookReading(**{'book_id': str(uuid.uuid4()), 'user_id': str(uuid.uuid4())})
    br.add()
    br.save()

    datas = storage.all()
    for key, data in datas.items():
        print(data)
