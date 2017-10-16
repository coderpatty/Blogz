from datetime import datetime
from flask import Flask, request, redirect, render_template, send_file
from flask_sqlalchemy import SQLAlchemy

#pylint: disable=no-member

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:Password@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    body = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __init__(self, title, body):
        self.title = title
        self.post = post
        self.body = body


tasks = []

@app.route('/', methods=['POST', 'GET'])
def index():
    bodystring = ""
    blogposts = Blog.query.order_by(Blog.pub_date).all()
    return render_template('index.html', object_list=blogposts)

@app.route('/new_post', methods=['POST', 'GET'])
def new_post():
    return render_template('new_post.html', title="Build-A-Blog!")

@app.route('/post', methods=['POST', 'GET'])
def post():

    if request.method == 'POST':
        title = request.form['title']
        entry = request.form['entry']
        blog_post = Blog(title, entry)
        db.session.add(blog_post)
        db.session.commit()
        return render_template('post.html', title=title, post_title=title, post_body=entry)

    if request.method == 'GET':
        post_id = request.args.get('id')
        this_post = Blog.query.get(int(post_id))
        title = this_post.title
        entry = this_post.post
        return render_template('post.html', title=title, post_title=title, post_body=entry)

if __name__ == '__main__':
    app.run()