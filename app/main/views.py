from . import main
from flask import app, render_template
from .forms import CreatePost
from app.main import forms
from ..logic import get_quotes


@main.route('/')
def index ():
  quote = get_quotes()
  return render_template('index.html',quote=quote)

@main.route('/create-post')
def addpost():
    title = 'post'
    form = CreatePost()
    return render_template('post.html',form = form,title = title)