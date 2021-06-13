DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS restaurants;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255)
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    restaurant_id INT REFERENCES restaurants(id) ON DELETE CASCADE,
    feedback TEXT
);

