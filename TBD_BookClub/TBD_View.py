from TBD_Models import *
from TBD_Controller import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('dummy.html')

@app.route('/admin')
def admin():
    return render_template('dummy.html')

@app.route('/admin/new_book')
def add_new_book():
    return render_template('dummy.html')

@app.route('/admin/stastics')
def show_stastics():
    return render_template('dummy.html')

@app.route('/admin/bookshelf')
def display_books():
    return render_template('dummy.html')

@app.route('/admin/wishlist')
def display_wishlist():
    return render_template('dummy.html')

@app.route('/admin/feedbacks')
def display_feedbacks():
    return render_template('dummy.html')