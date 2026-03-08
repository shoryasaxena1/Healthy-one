from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'healthy_one_secret_key'

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('healthy_one.db')
    c = conn.cursor()
    # User table: Stores profile, stats, and calories
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  username TEXT UNIQUE, 
                  password TEXT, 
                  age INTEGER, 
                  weight REAL, 
                  height REAL, 
                  gender TEXT,
                  maintenance_cals REAL)''')
    conn.commit()
    conn.close()

# --- CALORIE CALCULATOR LOGIC ---
def calculate_maintenance(weight, height, age, gender):
    # Mifflin-St Jeor Equation
    if gender.lower() == 'male':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return round(bmr * 1.2) # Sedentary multiplier as baseline

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    # Logic to save new user data
    pass

@app.route('/admin_vault', methods=['GET', 'POST'])
def admin_vault():
    if request.method == 'POST':
        if request.form.get('admin_pass') == 'Shaurya.78':
            conn = sqlite3.connect('healthy_one.db')
            users = conn.execute('SELECT * FROM users').fetchall()
            conn.close()
            return render_template('admin.html', users=users)
        else:
            flash("Access Denied: Incorrect Admin Password")
    return render_template('admin_login.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
