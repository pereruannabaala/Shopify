# E-Commerce System - Python Flask and SQLite and Daraja API

## Overview

This is a simple e-commerce system built using Python's Flask web framework and SQLite as the database. The application provides basic functionalities for both customers and administrators, including browsing products, placing orders, and viewing analytics. Daraja API was used for MPESA payments

## Features

### User Features

+ **Product Browsing:** Customers can view available products listed in the database.
+ **Product Search:** Customers can search for specific products using a search bar.
+ **Shopping Cart:** Customers can add products to their shopping cart.
+ **Order Placement:** Customers can place orders for the products in their cart.

### Admin Features
+ **Product Management:** Admins can view and manage the products available in the database.
+ **Order Management:** Admins can view and manage all customer orders.
+ **User Analytics:** Admins can see the number of customers who accessed the e-commerce platform.

## Installations

### Prerequisites
+ Python 3.x
+ Flask
+ SQLite

### Setup

1. Clone the repository
```python
git clone git@github.com:pereruannabaala/Shopify.git
cd Shopify
```

2. Activate virtual environment
```python
source shop_venv/bin/activate
```

3. Install the Required Packages
```python
pip install -r requirements.txt
```

4.Set up database
```python
flask db init
flask db migrate
flask db upgrade
```

5.Run the application
```python
flask run
```

## Database Structures
The system uses SQLite with the following key tables:
+ **Users**: Stores customer and admin login credentials.
+ **Products**: Contains details of available products such as name, description, price, and stock.
+ **Cart**: Contains details of the quantity,customer and product
+ **Orders**: Stores details of customer orders, including products purchased and order status.

## Admin Privileges
Admins have the ability to:
+ **Add Products**: Add new products to the system.
+ **Update Products**: Modify product details such as price or quantity.
+ **Delete Products**: Remove products from the inventory.
+ **View and Update Orders**: See customer orders and manage order statuses.
+ **Track Customer Activity**: View the number of customers accessing the platform.

## Contributing
Feel free to fork this repository and submit pull requests. Contributions, suggestions, and issues are welcome!

