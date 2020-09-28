from database.db import db


class Author(db.Document):
    name = db.StringField(required=True, unique=True, max_length=100)

class Article(db.DynamicDocument):
    title = db.StringField(required=True, max_length=200)
    text = db.StringField(required=True)
    author = db.ReferenceField(Author)
