#!/usr/bin/python3
# MELV_MYSQL_USER=getcho MELV_MYSQL_PWD=b51443a2338 MELV_MYSQL_HOST=localhost MELV_MYSQL_DB=mind_elevate MELV_TYPE_STORAGE=db ./insert_genres.py

from models import BookGenre
"""
genre = BookGenre(name="Technology")
genre3 = BookGenre(name="Religion")
genre4 = BookGenre(name="Science & Research")
genre5 = BookGenre(name="Enviroment")
genre6 = BookGenre(name="Academic & Education")
genre7 = BookGenre(name="Biography")
genre8 = BookGenre(name="Art")
genre9 = BookGenre(name="Fiction & Litrature")
genre10 = BookGenre(name="Business & Career")
genre11 = BookGenre(name="Health and Fitness")
genre12 = BookGenre(name="Lifestyle")
genre13 = BookGenre(name="Politics & Laws")

genre.add()
genre.save()


genre3.add()
genre3.save()


genre4.add()
genre4.save()

genre5.add()
genre5.save()
genre6.add()
genre6.save()
genre7.add()
genre7.save()
genre8.add()
genre8.save()
genre9.add()
genre9.save()
genre10.add()
genre10.save()
genre11.add()
genre11.save()
genre12.add()
genre12.save()
"""
genre = BookGenre(name="Politics & Laws")
genre.add()
genre.save()
