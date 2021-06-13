from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.review import Review
import repositories.review_repository as review_repository
import repositories.user_repository as user_repository
import repositories.restaurant_repository as restaurant_repository

reviews_blueprint = Blueprint("reviews", __name__)

@reviews_blueprint.route("/reviews")
def reviews():
    reviews = review_repository.select_all()
    return render_template("reviews/index.html", reviews = reviews)

    