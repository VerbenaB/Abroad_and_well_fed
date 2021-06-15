from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.restaurant import Restaurant

import repositories.restaurant_repository as restaurant_repository

restaurants_blueprint = Blueprint("restaurants", __name__)

@restaurants_blueprint.route("/restaurants")
def restaurants():
    restaurants = restaurant_repository.select_all()
    return render_template("restaurants/index.html", restaurants = restaurants)

@restaurants_blueprint.route("/restaurants/<id>")
def show(id):
    restaurant = restaurant_repository.select(id)
    users = restaurant_repository.users(restaurant)
    feedbacks_1 = restaurant_repository.feedback_1(restaurant)
    return render_template("restaurants/show.html", restaurant=restaurant, users=users, feedbacks_1=feedbacks_1)

@restaurants_blueprint.route("/restaurants/new", methods=['GET'])
def new_restaurant():
    return render_template("/restaurants/new.html")

@restaurants_blueprint.route("/restaurants", methods=['POST'])
def create_restaurant():
    name = request.form['name']
    category = request.form['category']
    new_restaurant = Restaurant(name, category)
    restaurant_repository.save(new_restaurant)
    return redirect("/restaurants")





