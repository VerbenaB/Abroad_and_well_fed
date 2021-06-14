from db.run_sql import run_sql
from models.review import Review

import repositories.user_repository as user_repository
import repositories.restaurant_repository as restaurant_repository


def save(review):
    sql = "INSERT INTO reviews(user_id, restaurant_id, feedback) VALUES (%s, %s, %s) RETURNING id"
    values = [review.user.id, review.restaurant.id, review.feedback]
    results = run_sql(sql, values)
    review.id = results[0]['id']
    return review

def select_all():
    reviews = []
    sql = "SELECT * FROM reviews"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        restaurant = restaurant_repository.select(row['restaurant_id'])
        review = Review(user, restaurant, row['feedback'], row['id'])
        reviews.append(review)
    return reviews

def select(id):
    review = None
    sql = "SELECT * FROM reviews WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        review = Review(result['user_id'], result['restaurant_id'], result ['feedback'], result['id'])
    return review 
    

def update(review):
    sql = "UPDATE reviews SET (user_id, restaurant_id, feedback) = (%s, %s, %s) WHERE id = %s"
    values = [review.user.id, review.restaurant.id, review.feedback, review.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM reviews"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM reviews WHERE id = %s"
    values = [id]
    run_sql(sql, values)
