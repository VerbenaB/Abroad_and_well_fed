from db.run_sql import run_sql
from models.restaurant import Restaurant
from models.user import User

def save(restaurant):
    sql = "INSERT INTO restaurants (name, category) VALUES (%s, %s) RETURNING id"
    values = [restaurant.name, restaurant.category]
    results = run_sql(sql, values)
    restaurant.id = results[0]['id']
    return restaurant

def select_all():
    restaurants = []
    sql = "SELECT * FROM restaurants"
    results = run_sql(sql)

    for row in results:
        restaurant = Restaurant(row['name'], row['category'], row['id'])
        restaurants.append(restaurant)
    return restaurants

def select(id):
    restaurant = None
    sql = "SELECT * FROM restaurants WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        restaurant = Restaurant(result['name'], result['category'], result['id'])
    return restaurant

def delete_all():
    sql = "DELETE FROM restaurants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM restaurants WHERE id = %s"
    values = [id]
    run_sql(sql, values)







