from . import main
from flask import app, render_template
from .forms import CreatePost
from app.main import forms


@main.route('/')
def index ():
  return render_template('index.html')

@main.route('/create-post')
def addpost():
    title = 'post'
    form = CreatePost()
    return render_template('post.html',form = form,title = title)