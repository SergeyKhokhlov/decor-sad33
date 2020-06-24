from flask import Flask, render_template, redirect, request, abort
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from data import __all_models, db_session, registration, users, search, figures
from random import choice
import sys
import os
from flask_restful import abort
from werkzeug.security import generate_password_hash, check_password_hash
import feedparser, json, os, datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pilorama_secretkey'  # Секретный ключ
login_manager = LoginManager()
login_manager.init_app(app)
sys.stdout.encoding  # 'UTF-8'


@login_manager.user_loader
def load_user(user_id):
    sessions = db_session.create_session()
    return sessions.query(users.User).get(user_id)


@app.route("/", methods=["GET", "POST"])
def index():
    form = search.SearchForm()
    sessions = db_session.create_session()
    figures_info = sessions.query(figures.Figure).all()
    names_figures = []
    prices_figures = []
    for i in figures_info:
        names_figures.append(i.name)
        prices_figures.append(i.price)
    if form.validate_on_submit():
        text = form.search_block.data
        return redirect("/search/" + text)
    return render_template("index.html", form=form, names_figures=names_figures,
                           prices_figures=prices_figures)


@app.route("/search/<string:text>", methods=["GET", "POST"])
def searching(text):
    form = search.SearchForm()
    sessions = db_session.create_session()
    figures_info = sessions.query(figures.Figure).all()
    names_figures = []
    prices_figures = []
    images_figures = []
    for i in figures_info:
        if text.lower() in i.name.lower():
            for j in i.name.lower().split():
                if text.lower() == j.lower():
                    names_figures.append(i.name)
                    prices_figures.append(i.price)
                    images_figures.append(i.images)
    if form.validate_on_submit():
        text_new = form.search_block.data
        return redirect("/search/" + text_new)
    return render_template("search.html", form=form, names_figures=names_figures,
                           images_len=len(images_figures), text=text,
                           prices_figures=prices_figures, images_figures=images_figures)


def main():
    db_session.global_init("db/blogs.db")
    app.run(port=2507)


if __name__ == '__main__':
    main()
