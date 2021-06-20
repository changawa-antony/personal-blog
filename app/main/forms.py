from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField,validators
from wtforms.validators import Required

class CreatePost(FlaskForm):
    topic = StringField(u'Topic', [validators.required(), validators.length(max=200)])
    content = TextAreaField(u'Content', [validators.optional(), validators.length(max=200)])
    submit = SubmitField('Post')
    