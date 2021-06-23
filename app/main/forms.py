from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField,validators
from wtforms.validators import Required

class CreatePost(FlaskForm):
    name = StringField(u'Topic', [validators.required(), validators.length(max=200)])
    comment = TextAreaField(u'Content', [validators.optional(), validators.length(max=200)])
    submit = SubmitField('Post')
    