# https://dev.to/paurakhsharma/flask-rest-api-part-1-using-mongodb-with-flask-3g7d
# https://www.youtube.com/watch?v=dpJ4B7jbmgo
from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Article, Author
from mongoengine import NotUniqueError
from mongoengine.queryset.visitor import Q


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/articles-bag'
}

initialize_db(app)

@app.route('/articles', methods=['POST', 'GET'])
def add_get_article():
    if request.method == 'POST':
        body = request.get_json()
        try:
            author = Author(name=body['author']).save()
        except NotUniqueError:
            author = Author.objects(name=body['author']).get()

        article = Article(
            title=body['title'],
            text=body['text'],
            author=author
        ).save()

        id = article.id
        return {'id': str(id)}, 200

    if request.method == 'GET':
        articles = Article.objects().to_json()
        return Response(articles, mimetype="application/json", status=200)

@app.route('/article/<id>', methods=['PUT', 'DELETE', 'GET'])
def update_get_article(id):
    if request.method == 'PUT':
        body = request.get_json()
        try:
            author = Author(name=body['author']).save()
        except NotUniqueError:
            author = Author.objects(name=body['author']).get()
        
        article = Article(
            title=body['title'],
            text=body['text'],
            author=author
        ).save()

        id = article.id
        return {'id': str(id)}, 200

    if request.method == 'DELETE':
        # delete author who has no articles?
        Article.objects.get(id=id).delete()
        return '', 200

    if request.method == 'GET':
        articles = Article.objects.get(id=id).to_json()
        return Response(articles, mimetype="application/json", status=200)

@app.route('/articles/search/<string:keyword>')
def search(keyword):
    author_result = Author.objects.filter(name__contains=keyword)

    result = Article.objects.filter(
            Q(text__contains=keyword) | 
            Q(title__contains=keyword) |
            Q(author__in=author_result)
            ).to_json()

    return Response(result, mimetype="application/json", status=200)

app.run()