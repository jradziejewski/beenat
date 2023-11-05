from flask import Flask
import psycopg2

app = Flask(__name__)

# Connect to the database
conn = psycopg2.connect(
    database="beenat", user="postgres", password="root", host="localhost", port="5432"
)

# create a cursor
cur = conn.cursor()

# if you already have any table or not id doesnt matter this
# will create a products table for you.
cur.execute(
    """CREATE TABLE IF NOT EXISTS products (id serial PRIMARY KEY, name varchar(100), price float);"""
)

# Insert some data into the table
cur.execute(
    """INSERT INTO products (name, price) VALUES ('Apple', 1.99), ('Orange', 0.99), ('Banana', 0.59);"""
)

# commit the changes
conn.commit()

# close the cursor and connection
cur.close()
conn.close()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/huj")
def huj():
    return "<h1>Huj</h1>"
