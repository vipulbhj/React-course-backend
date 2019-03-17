from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/api/social-media-handles')
@cross_origin()
def social_media_handles():
    smh = jsonify({
        "data": [
            {
                "name": "Facebook",
                "link": "https://facebook.com"
            },
            {
                "name": "Github",
                "link": "https://github.com"
            },
            {
                "name": "Twitter",
                "link": "https://twitter.com"
            },
            {
                "name": "Linkedin",
                "link": "https://linkedin.com"
            }
        ]
    })

    return smh


@app.route('/api/blogs')
@cross_origin()
def blogs():
    blogs = jsonify({
        "data": [
            {
                "id": 1,
                "name": "My first Blog",
                "data": "In this blog, I talk about how to build react apps which can be extended to uses erver data later"
            },
            {
                "id": 2,
                "name": "Travel Blog One",
                "data": "In this blog, I talk about how to build react apps which can be extended to uses erver data later"
            },
            {
                "id": 3,
                "name": "Day in the life of Web Dev",
                "data": "In this blog, I talk about how to build react apps which can be extended to uses erver data later"
            },
            {
                "id": 4,
                "name": "Code with Vipul",
                "data": "In this blog, we are going to code together some new and interesting things, In this blog, we are going to code together some new and interesting things, In this blog, we are going to code together some new and interesting things, In this blog, we are going to code together some new and interesting things"
            },
            {
                "id": 5,
                "name": "Code with Vipul",
                "data": "In this blog, we are going to code together some new and interesting things, In this blog, we are going to code together some new and interesting things, In this blog, we are going to code together some new and interesting things, In this blog, we are going to code together some new and interesting things"
            }
        ]
    })

    return blogs


