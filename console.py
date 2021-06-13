import pdb
from models.restaurant import Restaurant
from models.user import User
from models.review import Review

import repositories.restaurant_repository as restaurant_repository
import repositories.user_repository as user_repository
import repositories.review_repository as review_repository

user_repository.delete_all()
restaurant_repository.delete_all()
review_repository.delete_all()

user1 = User('Marco')
user_repository.save(user1)

user2 = User('Elena')
user_repository.save(user2)

user3 = User('Maddalena')
user_repository.save(user3)

user4 = User('Simone')
user_repository.save(user4)


restaurant1 = Restaurant('Razzo', 'pizza')
restaurant_repository.save(restaurant1)

restaurant2 = Restaurant('Paesano', 'pizza')
restaurant_repository.save(restaurant2)

restaurant3 = Restaurant('French Consulate Cafe', 'espresso')
restaurant_repository.save(restaurant3)

restaurant4 = Restaurant('Lovecrumbs', 'espresso')
restaurant_repository.save(restaurant4)

restaurant5 = Restaurant('Gaia', 'aperitivo')
restaurant_repository.save(restaurant5)

restaurant6 = Restaurant('I polentoni', 'aperitivo')
restaurant_repository.save(restaurant6)

review1 = Review(user1, restaurant1, '4.5 stars, Excellent pizza Napoli style, pity it is only takeaway')
review_repository.save(review1)

review2 = Review(user2, restaurant2, '5 stars, Excellent atmoshpere, seems like home')
review_repository.save(review2)

review3 = Review(user1, restaurant3, '4 stars, Decent price for an espresso')
review_repository.save(review3)

review4 = Review(user3, restaurant4, '3.5 stars, Good vibes, excellent cake selection, good coffee, in line with Edinburgh prices')
review_repository.save(review4)

review5 = Review(user4, restaurant4, '3 stars, Cute place but I average coffe')
review_repository.save(review1)

review6 = Review(user3, restaurant5, '4.5 stars, Tiny place on Leith street that offers Sicilian delicatesse at good price. Lovely owners')
review_repository.save(review6)

review7 = Review(user4, restaurant1, '5 stars, Great pizza selection, my go-to pizzeria')
review_repository.save(review1)

review8 = Review(user1, restaurant6, '4 stars, excelletn selection for an aperitivo at competitive prices')
review_repository.save(review1)

restaurants = user_repository.restaurants(user1)


pdb.set_trace()

