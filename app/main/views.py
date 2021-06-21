from app.auth.forms import LoginForm
from flask.helpers import url_for
from werkzeug.utils import redirect
from app.models import Post
from . import main
from flask import app, render_template,request
from .forms import CreatePost
from app.main import forms
from ..logic import get_quotes
from flask_login import login_required
from ..auth import views
from ..models import Quote, db 
from ..auth import views

posts = Post
quote = Quote

@main.route('/')
def index ():
      
  quote = get_quotes()
  show_posts = Post.get_posts()
  return render_template('index.html',quote=quote, show_post = show_posts)

@main.route('/create-post', methods = ['GET', 'POST'])
@login_required
def addpost():
      
    login_form = views.login
    title = 'post'
    form = CreatePost()

    if request.method == 'POST':
        post = Post(title = form.title.data, content = form.content.data)
        post.save_post()
        return redirect(url_for('index.html'))
        
    return render_template('post.html',form = form,title = title, login_form = login_form)
