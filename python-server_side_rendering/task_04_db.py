#!/usr/bin/python3
"""
Flask application that reads and displays product data from JSON, CSV, or SQLite.
Supports filtering by product ID and handles various edge cases.
"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json_file(filepath):
    """
    Read and parse data from a JSON file.
    """
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def read_csv_file(filepath):
    """
    Read and parse data from a CSV file.
    """
    try:
        products = []
        with open(filepath, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert id to int and price to float
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
        return products
    except FileNotFoundError:
        return None
    except (ValueError, KeyError):
        return None


def read_sql_database(database):
    """
    Read and parse data from a SQLite database.
    """
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        # Fetch all products from the Products table
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        # Convert to list of dictionaries
        products = []
        for row in rows:
            product = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products.append(product)
        
        conn.close()
        return products
    except sqlite3.Error:
        return None


@app.route('/products')
def products():
    """
    Display products from JSON, CSV, or SQLite database based on source parameter.
    Supports optional filtering by product ID.
    """
    # Get query parameters
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read data from appropriate source
    if source == 'json':
        products_data = read_json_file('products.json')
    elif source == 'csv':
        products_data = read_csv_file('products.csv')
    else:  # source == 'sql'
        products_data = read_sql_database('products.db')
    
    # Check if data was successfully read
    if products_data is None:
        return render_template('product_display.html', 
                             error="Error reading data source")
    
    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_data if p['id'] == product_id]
            
            if not filtered_products:
                return render_template('product_display.html', 
                                     error="Product not found")
            
            products_data = filtered_products
        except ValueError:
            return render_template('product_display.html', 
                                 error="Invalid product ID")
    
    # Render template with products data
    return render_template('product_display.html', products=products_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)