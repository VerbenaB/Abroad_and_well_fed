from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
import repositories.user_repository as user_repository

users_blueprint = Blueprint("users", __name__)

# INDEX
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("user/index.html", users = users)



