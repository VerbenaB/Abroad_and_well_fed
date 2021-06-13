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

    
