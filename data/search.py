from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm


class SearchForm(FlaskForm):
    search_block = StringField()
    search_btn = SubmitField('Поиск')
