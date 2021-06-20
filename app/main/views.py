from . import main
from flask import app, render_template


@main.route('/')
def index ():
  return render_template('index.html')