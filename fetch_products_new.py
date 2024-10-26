from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_new.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    category = request.form['category']
    connection = None  # Initialize the connection variable
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="Vivek",  # Update with your MySQL username
            password="Vivek@2004",  # Update with your MySQL password
            database="veg_shopping_db"  # Update with your database name
        )
        cursor = connection.cursor()

        query = "SELECT product_name, price, brand FROM veg_products WHERE category = %s"
        cursor.execute(query, (category,))
        veg_products = cursor.fetchall()

        if veg_products:
            return render_template('results_new.html', veg_products=veg_products, category=category)
        else:
            return render_template('results_new.html', veg_products=None, category=category)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "Database connection failed."

    finally:
        if connection and connection.is_connected():  # Check if connection is initialized and open
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
