from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_screen():
  return render_template('home.html', site_name="SmartDuck")

@app.route('/login')
def login():
  return render_template('login.html', site_name="SmartDuck")

@app.route('/signup')
def signup():
  return render_template('signup.html', site_name="SmartDuck")

@app.route('/maths')
def maths():
  return render_template('maths.html', site_name="SmartDuck")

@app.route('/chemistry')
def chemistry():
  return render_template('chemistry.html', site_name="SmartDuck")

@app.route('/physics')
def physics():
  return render_template('physics.html', site_name="SmartDuck")

@app.route('/about_us')
def about_us():
  return render_template('about_us.html', site_name="SmartDuck")

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html', site_name="SmartDuck")

@app.route('/chem_periodic_table')
def periodic_table():
  return render_template('chem_table.html', site_name="SmartDuck")

app.run(host='0.0.0.0', port=81, debug=True)

