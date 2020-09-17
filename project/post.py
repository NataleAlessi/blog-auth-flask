from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post
from . import db

post = Blueprint('post', __name__)


@post.route('/index')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@post.route('/<int:post_id>')
def show_post(post_id):
    post = Post.query.get(post_id)
    return render_template('post.html', post=post)


@post.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Title is required!')
        else:
            new_post = Post(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('post.index'))
    return render_template('create.html')


@post.route('/<int:post_id>/edit', methods=('GET', 'POST'))
@login_required
def edit(post_id):
    post = Post.query.get(post_id)
    if request.method == 'POST': #needs error handling
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Title is required!')
        else:
            post.content = content
            db.session.commit()
            return redirect(url_for('post.index'))
    return render_template('edit.html', post=post)


@post.route('/<int:post_id>/delete', methods=('POST',))
@login_required
def delete(post_id):
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post was successfully deleted!')
    return redirect(url_for('index'))

