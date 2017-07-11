from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'secret'
mysql = MySQLConnector(app, 'emailvalidationdb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # flash error message
    return redirect('/')

@app.route('/success')
def display_emails():
    # flash success message
    return render_template('success.html')

app.run(debug=True)