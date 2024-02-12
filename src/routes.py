from flask import render_template ,url_for,flash,redirect,request,session
from . import app
import os



# @app.route("/")
@app.route('/login', methods=['POST', 'GET'])
def login():
     
    return render_template('login.html')




# Registration Routes

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        flash('Registration successful. You can now log in.', 'success')
        

    return render_template('registration.html')

# Log our route 
@app.route('/logout')
def logout():
    # Clear the session
    session.clear()

    # Redirect to the login page
    flash('Logout successful', 'success')
    return redirect(url_for('login'))

# App routes
  
@app.route('/')
def home():
    if 'uid' in session:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))
    

    
@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')


