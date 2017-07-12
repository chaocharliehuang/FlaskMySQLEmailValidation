from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'secret'
mysql = MySQLConnector(app, 'emailvalidationdb')

@app.route('/')
def index():
    if 'email' not in session:
        session['email'] = ''
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    submitted_email = request.form['email']
    session['email'] = submitted_email

    data = {'email': submitted_email}
    query = "SELECT * FROM emails WHERE email = :email LIMIT 1"
    user = mysql.query_db(query, data)
    if len(user) != 0:
        return redirect('/success')
    else:
        flash('Email is not valid!')
        return redirect('/')

@app.route('/success')
def display_emails():
    flash('The email address you entered (' + session['email'] + ') is a VALID email address! Thank you!')

    query = "SELECT email, DATE_FORMAT(created_at, '%m/%d/%y %l:%i%p') AS created FROM emails ORDER BY created DESC"
    emails = mysql.query_db(query)
    return render_template('success.html', emails=emails)

app.run(debug=True)