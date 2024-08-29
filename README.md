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
+ **Order Management:** Admins can view all customer orders.
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
