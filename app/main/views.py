from app.auth.forms import LoginForm
from flask.helpers import url_for
from werkzeug.utils import redirect
from app.models import Post
from . import main
from flask import render_template,request,flash
from .forms import CreatePost
from ..logic import get_quotes,show_post
from flask_login import login_required
from ..auth import views
from ..models import Quote, db 
from ..auth import views

posts = Post
quote = Quote

@main.route('/')
def index():
      
  quote = get_quotes()
  show_posts = Post.get_posts
  return render_template('index.html',quote=quote, show_post = show_posts)

@main.route('/create-post', methods = ['GET', 'POST'])
@login_required
def addpost():
      
    login_form = views.login
    title = 'post'
    form = CreatePost()

    if request.method == 'POST':
        topic = form.topic.data
        content = form.content.data
        post = Post(topic,content)
        post.save_post()
        db.session.add(post)
        db.session.commit()
        flash('Post was successfully added')
        return redirect(url_for('index'))
        
    return render_template('post.html',form = form,title = title, login_form = login_form)
