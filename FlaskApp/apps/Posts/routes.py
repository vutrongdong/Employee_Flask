from flask import render_template
from FlaskApp import app
from FlaskApp.apps.Posts import controller

# list port
@app.route("/")
def list_post():
    return controller.index()

# detail post
@app.route("/post/<int:post_id>")
def post(post_id):
    return controller.detail(post_id)

# create post
@app.route("/post/new", methods=['GET', 'POST'])
def new_post():
    return controller.create()

# update post
@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    return controller.update(post_id)


# delete post
@app.route("/post/<int:post_id>/delete", methods=['GET', 'POST'])
def delete_post(post_id):
    return controller.delete(post_id)
