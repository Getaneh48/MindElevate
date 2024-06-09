#!/usr/bin/python3
#MELV_MYSQL_USER=getcho MELV_MYSQL_PWD=b51443a2338 MELV_MYSQL_HOST=localhost MELV_MYSQL_DB=mind_elevate MELV_TYPE_STORAGE=db ./main-2.py

from models import storage, User, Book, BookReading, Friend, FriendRequest, ReadingLog, BookmarkBook,\
FavouriteBook, Badge
import json

# create user object and save it
# user_dict = {'username':'biniyam', 'password':'454', 'first_name':'biniyam', 'last_name':'arega', 'age':34, 'sex':'M'}

# user = User(**user_dict)
# storage.new(user)
# storage.save()

# create book object and save it

#book_d = {'title': 'Python for dummies', 'author': 'Allan Smith', 'genere': 'Education', 'pub_year': 2016, 'pages': 650}

#book = Book(**book_d)
#storage.add(book)
#storage.save()

# user_id = 4a2fa583-5080-49c8-9061-ef217bc42778
# friend_id = 24b40bd3-2262-4fa3-a3cb-5abea29921c7
# book_id = ac6a6811-0aad-45fb-b082-d6e5a1f8c7a1

book_rd = {
    'user_id': '4a2fa583-5080-49c8-9061-ef217bc42778',
    'book_id': 'ac6a6811-0aad-45fb-b082-d6e5a1f8c7a1',
    'pages_per_day': 20,
    'hours_per_day': 4,
    'expected_completion_day': 10
    }

#friend = Friend(user_id='4a2fa583-5080-49c8-9061-ef217bc42778', friend_id='1a61ca49-c1fb-47d4-80b3-efbdb2456033')
#storage.add(friend)
#friend.save()

# bookr = BookReading(**book_rd)
# storage.add(bookr)
# storage.save()

# get all users and their friends
"""
users = storage.all(User)
for user in users.values():
    if user.friends:
        print(f"User: {user.username}")
        for friend in user.friends:
            frd = storage.get('User', friend.friend_id)
            if frd is not None:
                print(f"{frd.first_name} {frd.last_name}")

"""

"""
fr = FriendRequest(request_from='4a2fa583-5080-49c8-9061-ef217bc42778', request_to='1a61ca49-c1fb-47d4-80b3-efbdb2456033', status='pending')

fr.add()
fr.save()
"""

"""
uid = '1a61ca49-c1fb-47d4-80b3-efbdb2456033'
user = storage.get('User', uid)
print(user.friends)
print(user.friend_requests)
"""

# gets all the book reads by a user

# user = storage.get('User', '4a2fa583-5080-49c8-9061-ef217bc42778')
# for bread in user.booksreading:
    # print(bread.books)
    # print(bread.reading_logs)

# add a reading log to a specific book being read
# rlog = ReadingLog(br_id='4eee4b89-6867-4efc-8172-cedc94f241bb',pages_read=20, hours_read=2, badge_id=None)
# rlog.add()
# rlog.save()

# bookmark a book
#bookmark = BookmarkBook(book_id='ac6a6811-0aad-45fb-b082-d6e5a1f8c7a1', bookmarked_by='4a2fa583-5080-49c8-9061-ef217bc42778')
#bookmark.add()
#bookmark.save()

# fav = FavouriteBook(book_id='ac6a6811-0aad-45fb-b082-d6e5a1f8c7a1', user_id='4a2fa583-5080-49c8-9061-ef217bc42778')
#fav.add()
# fav.save()


# user = storage.get('User', '4a2fa583-5080-49c8-9061-ef217bc42778')
# if user.bookmarked_books:
    # for bbks in user.bookmarked_books:
        # print(bbks.book)

# user = storage.get('User', '4a2fa583-5080-49c8-9061-ef217bc42778')
# print(user.favourite_books[0].book)

# badge = Badge(btype="Daily Goal", icon="images/daily_badge.png", description="a reward given for the user when they achieve their daily goal")

# badge.add()
# badge.save()

# add a reading log to a specific book being read
# rlog = ReadingLog(br_id='4eee4b89-6867-4efc-8172-cedc94f241bb',pages_read=10, hours_read=1, badge_id='de86102b-a428-4497-a879-72caebd2caaf')
# rlog.add()
# rlog.save()

# user = storage.get('User', '4a2fa583-5080-49c8-9061-ef217bc42778')
#for bread in user.booksreading:
    #print(bread.book)
    #print(bread.reading_logs)
    #print(bread.reading_logs[0].badge)

# adds book reading
# reading = BookReading(user_id='4a2fa583-5080-49c8-9061-ef217bc42778', book_id='cc064473-aafb-4af2-ba6b-6b293cfc5e4c', pages_per_day=10, hours_per_day=2, expected_completion_day=18)

#reading.add()
#reading.save()

# get currently reading books of a user that are on progress
#user = storage.get('User', '4a2fa583-5080-49c8-9061-ef217bc42778')
#result = storage.readingOnProgress(user)
#for r in result:
    #print(json.dumps(r.to_dict()))

# badges categories 'daily' 'book completion' 'challenge win'
#badge = Badge(**{'btype':'Novel Conqueror', 'description': 'Earned by conquering one book after another.'})

#badge.add()
#badge.save()

badge = storage.badge_by_type('page turner')
print(badge)
