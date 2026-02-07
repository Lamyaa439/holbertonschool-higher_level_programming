#!/usr/bin/python3
"""
Flask application that reads and displays product data from JSON or CSV files.
Supports filtering by product ID and handles various edge cases.
"""
from flask import Flask, render_template, request
import json
import csv

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


@app.route('/products')
def products():
    """
    Display products from JSON or CSV file based on source parameter.
    Supports optional filtering by product ID.
    """
    # Get query parameters
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read data from appropriate file
    if source == 'json':
        products_data = read_json_file('products.json')
    else:  # source == 'csv'
        products_data = read_csv_file('products.csv')
    
    # Check if data was successfully read
    if products_data is None:
        return render_template('product_display.html', 
                             error="Error reading data file")
    
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