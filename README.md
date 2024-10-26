# Shopping-Assistant
This project is a simple shopping assistant web application built with Flask and MySQL. It allows users to search and view a list of vegetarian products filtered by category, along with their prices and brands. This app demonstrates the integration of a Flask web application with a MySQL database, focusing on retrieving and displaying categorized product data. The database stores vegetarian products with prices in rupees, enabling easy access and management for users.

Features:
Fetches data from a MySQL database for vegetarian products.
Displays the products filtered by category in a web-based table format.
Aimed to serve as a foundational project for learning SQL, Flask, and web application integration.
Project Structure and File Descriptions
1. fetch_products_new.py
Description: This is the main Flask application file that handles the backend logic of the application. It includes the routes to render HTML templates and interact with the MySQL database to fetch and display the product information.
Key Functions:
Database Connection: Connects to a MySQL database using the provided credentials.
Fetch Data: Defines a route to fetch and display vegetarian products by category.
Error Handling: Manages cases where a connection might fail or the template is missing.
2. results.html
Description: The HTML template responsible for displaying the fetched product data. This file uses Jinja2 templating to dynamically display data fetched from the MySQL database in a structured table format.
Key Sections:
Header: Displays the selected category of products.
Table: Lists each product’s name, price (in rupees), and brand in a user-friendly tabular format.
Styling: Basic CSS styling to enhance readability and usability.
3. requirements.txt
Description: Contains a list of all the necessary Python libraries and dependencies required to run the application. This file is useful for setting up the environment by installing the dependencies via pip.
Key Libraries:
Flask: Web framework used for building the application.
mysql-connector-python: Library to connect the Flask app with the MySQL database.
