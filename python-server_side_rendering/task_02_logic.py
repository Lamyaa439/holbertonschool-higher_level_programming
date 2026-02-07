#!/usr/bin/python3
"""
Flask application with dynamic templates using loops and conditions.
Reads data from JSON file and displays it dynamically.
"""
from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """
    Render the items page with data from JSON file.
    Reads items from items.json and passes them to the template.
    """
    try:
        # Read data from JSON file
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except FileNotFoundError:
        # If file doesn't exist, use empty list
        items_list = []
    except json.JSONDecodeError:
        # If JSON is invalid, use empty list
        items_list = []
    
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)