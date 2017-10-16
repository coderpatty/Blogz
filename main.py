from datetime import datetime
from flask import Flask, request, redirect, render_template, send_file
from flask_sqlalchemy import SQLAlchemy

#pylint: disable=no-member

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:Password@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

if __name__ == '__main__':
    app.run()