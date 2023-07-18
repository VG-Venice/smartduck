from flask import Flask, render_template, request
from database import engine, getPeriodicTableDataset, add_account_to_db
from sqlalchemy import text

app = Flask(__name__)


def el_import(id):
  with engine.connect() as conn:
    info = conn.execute(text("select * from elementsinfo"))
  info_dict = []
  for el_row in info.all():
    info_dict.append(({
      "Atomic Number": el_row.atomic_no,
      "Symbol": el_row.symbol,
      "Name": el_row.name,
      "Valency": el_row.valency,
      "Group Number": el_row.group_no,
      "Period Number": el_row.period_no,
      "State(Room temp.)": el_row.state_rt,
      "Element Type": el_row.eType
    }))
  return info_dict

def load_element_from_db(id):
  with engine.connect() as conn:
    info = conn.execute(text(f"SELECT * FROM elementsinfo WHERE id ={id}"))
    rows = []
    for row in info.all():
      rows.append(({
      "Atomic Number": row.atomic_no,
      "Symbol": row.id,
      "Name": row.name,
      "Valency": row.valency,
      "Group Number": row.group_no,
      "Period Number": row.period_no,
      "State(Room temp.)": row.state_rt,
      "Element Type": row.eType
      }))
    if len(rows) == 0:
      return None
    else:
      return row

@app.route('/')
def home_screen():
  return render_template('home.html', site_name="SmartDuck")


@app.route('/login', methods=['post'])
def login():
  data = request.form
  add_account_to_db(data)
  return render_template('login.html', site_name="SmartDuck", accountinfo = data)


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
  el_import(id)
  return render_template(
    'chem2_table.html',
    site_name="SmartDuck",
    pTable=pTable,
    id = id
  )


@app.route('/el_information/<id>')
def info_show(id):
    importer = load_element_from_db(id)
    return render_template('clicked_info.html',
                         site_name="SmartDuck",
                         importer = importer
                        )

app.run(host='0.0.0.0', port=81, debug=True)
