from flask import render_template
from FlaskApp import app
from FlaskApp.apps.Controllers import PostController

# list port
@app.route("/")
def list_post():
    return PostController.index()

# detail post
@app.route("/post/<int:post_id>")
def post(post_id):
    return PostController.detail(post_id)

# create post
@app.route("/post/new", methods=['GET', 'POST'])
def new_post():
    return PostController.create()

# update post
@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    return PostController.update(post_id)


# delete post
@app.route("/post/<int:post_id>/delete", methods=['GET', 'POST'])
def delete_post(post_id):
    return PostController.delete(post_id)
