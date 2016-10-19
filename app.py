import json
from flask import Flask, request

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

@app.route('/')
def hello_world():
    return json.dumps(posts)

@app.route('/addpost', methods=["POST"])
def add_post():
    # request.arg dung de get, request.form lay post
    args = request.form
    title = args["title"]
    content = args["content"]
    new_post = {"title": title,
                "content": content}
    posts.append(new_post)
    print(title, content)
    return "OK"


if __name__ == '__main__':
    app.run()
