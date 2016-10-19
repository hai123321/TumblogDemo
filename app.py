import json
from flask import Flask

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


if __name__ == '__main__':
    app.run()
