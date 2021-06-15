from controllers.review_controller import reviews

from flask import Flask, render_template
from flask import Blueprint

from models.user import User

import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

# INDEX
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/index.html", users = users)

# SHOW
@users_blueprint.route("/users/<id>")
def show(id):
    user = user_repository.select(id)
    restaurants = user_repository.restaurants(user)
    feedbacks = user_repository.feedback(user)
    return render_template("users/show.html", user=user, restaurants=restaurants, feedbacks=feedbacks)




