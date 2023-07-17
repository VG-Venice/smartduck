from flask import Flask, render_template
from database import engine, getPeriodicTableDataset
from sqlalchemy import text

app = Flask(__name__)


def el_import():
  with engine.connect() as conn:
    info = conn.execute(text("select * from elementsinfo"))
  info_dict = []
  for el_row in info.all():
    info_dict.append(({
      "Atomic Number": el_row.atomic_no,
      "Symbol": el_row.id,
      "Name": el_row.name,
      "Valency": el_row.valency,
      "Group Number": el_row.group_no,
      "Period Number": el_row.period_no,
      "State(Room temp.)": el_row.state_rt,
      "Element Type": el_row.eType
    }))
  return info_dict


@app.route('/')
def home_screen():
  return render_template('home.html', site_name="SmartDuck")


@app.route('/login')
def login():
  return render_template('login.html', site_name="SmartDuck")


@app.route('/signup')
def signup():
  return render_template('signup.html', site_name="SmartDuck")


@app.route('/about_us')
def about_us():
  return render_template('about_us.html', site_name="SmartDuck")


@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html', site_name="SmartDuck")


@app.route('/chem_periodic_table')
def periodic_table():
  pTable = getPeriodicTableDataset()
  el_import()
  return render_template(
    'chem2_table.html',
    site_name="SmartDuck",
    pTable=pTable
  )


@app.route('/el_information/<int:atomic_no>')
def info_show(atomic_no):
  importer = el_import()
  return importer[atomic_no-1]


app.run(host='0.0.0.0', port=81, debug=True)
