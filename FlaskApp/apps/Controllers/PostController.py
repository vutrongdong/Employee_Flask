from FlaskApp.apps.Repositories.Posts.post import *
from flask import render_template, url_for, flash, redirect, request, abort
from FlaskApp.apps.Forms.PostForm import PostForm

# index post
def index():
    posts= Post.query.all()
    return render_template('Posts/list.html', posts=posts)
# detail post
def detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('Posts/detail.html', title="post.title", post=post)
# create post
def create():
    form = PostForm()
    if form.validate_on_submit():
        flash('Thêm bài viết thành công!', 'success')
        post = Post(title = form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('list_post'))
    return render_template('Posts/form.html', title='New Post', form=form, lagend=" Create Post")
# update post
def update(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit() 
        flash('Cập nhật bài viết thành công!', 'success')
        return redirect(url_for('post', post_id= post.id))
    elif request.method =='GET':
        form.title.data = post.title
        form.content.data = post.content

    return render_template('Posts/form.html', title='Update Post', form=form, lagend=" Update Post")
# delete post
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Xóa bài viết thành công!', 'success')
    return redirect(url_for('list_post'))