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

# NEW
@reviews_blueprint.route("/reviews/new", methods=['GET'])
def new_review():
    users = user_repository.select_all()
    restaurants = restaurant_repository.select_all()
    return render_template("reviews/new.html", users=users, restaurants=restaurants)

# CREATE
@reviews_blueprint.route("/reviews", methods=['POST'])
def create_review():
    user_id = request.form['user_id']
    restaurant_id =request.form['restaurant_id']
    feedback = request.form['feedback']
    user = user_repository.select(user_id)
    restaurant = restaurant_repository.select(restaurant_id)
    review = Review(user, restaurant, feedback)
    review_repository.save(review)
    return redirect ('/reviews')

# EDIT
@reviews_blueprint.route("/reviews/<id>/edit")
def edit_review(id):
    review = review_repository.select(id)
    users = user_repository.select_all()
    restaurants = restaurant_repository.select_all()
    return render_template("reviews/edit.html", review=review, users=users, restaurants=restaurants)


# DELETE
@reviews_blueprint.route("/reviews/<id>/delete", methods=['POST'])
def delete_review(id):
    review_repository.delete(id)
    return redirect ('/reviews')




    