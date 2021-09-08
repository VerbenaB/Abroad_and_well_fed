# Abroad and Well Fed
A web application to review Italian restaurants abroad.

## Running instructions
Clone down the repo.

Install Flask (https://flask.palletsprojects.com/en/2.0.x/installation/).

Install psycopg2 (https://pypi.org/project/psycopg2/).

Navigate to wherever you stored the restaurant's reviews directory in your command line.

createdb Italian_restaurants

psql -d Italian_restaurants -f db/Italian_restaurants.sql

python3 console.py

q (to quit pdb)

flask run

Copy the address where the app is running into your browser’s address bar

### Techonologies used
Python, Flask, psycopg2, postgreSQL, SQL, HTML, CSS
