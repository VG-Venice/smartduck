from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_screen():
  return render_template('home.html', site_name="SmartyNotes")

@app.route('/login')
def login():
  return render_template('login.html', site_name="SmartyNotes")

@app.route('/signup')
def signup():
  return render_template('signup.html', site_name="SmartyNotes")

app.run(host='0.0.0.0', port=81, debug=True)