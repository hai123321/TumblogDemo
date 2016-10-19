from mongoengine import *
from mlab import *
import json
from flask import *

app = Flask(__name__)

post1 = {
    "title": "Good day",
    "content": "Today I met a girl. Fking noob"
}

post2 = {
    "title": "Bad day",
    "content": "Today I met a Dumb Boy. Fking Retard"
}

print(post1["title"])
print(post1["content"])

print(post2["title"])
print(post2["content"])

posts = [post1, post2]


class Post(Document):
    title = StringField()
    content = StringField()

    def get_json(self):
        return {"title": self.title, 'content': self.content}


@app.route('/')
def hello_world():
    posts = Post.objects
    return jsonify([post.get_json() for post in posts])


@app.route('/addpost', methods=["POST"])
def add_post():
    # request.arg dung de get, request.form lay post
    args = request.form
    title = args["title"]
    content = args["content"]

    p = Post(title=title, content=content)
    p.save()
    return jsonify({"code": 1, "message": "OK"})


if __name__ == '__main__':
    mlab_connect()
    app.run()
