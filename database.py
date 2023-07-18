from sqlalchemy import create_engine, text
import os

db_conn_str = os.environ['DB_CONN_STR']

engine = create_engine(db_conn_str,
  connect_args={"ssl": {
    "ssl_ca": "cert.pem"
  }})

def getPeriodicTableDataset():
  _rows = 10
  _cols = 18

  pTable = [['' for x in range(_cols)] for y in range(_rows)]

  for p in range(_rows):
    with engine.connect() as conn:
      periodResult = conn.execute(
        text(f"select * from elementsinfo where posRow={p}"))
    for pr in periodResult:
      pTable[pr.posRow][pr.posCol] = str(pr.atomic_no) +'-'+ pr.symbol +'-'+ pr.name +'-'+ pr.eType + '-'+ str(pr.valency)
  return pTable

def add_account_to_db(data):
  with engine.connect() as conn:
      conn.execute(
        text(
          f"INSERT INTO accounts (full_name, user_name, user_email, pass_word) VALUES('{data['fullname']}', '{data['username']}',  '{data['email']}', '{data['password']}')"
        ))  
# def clicked_element():
#   with engine.connect() as conn:
#     info = conn.execute(text("select * from elementsinfo"))
#   info_dict = []
#   for el_row in info.all():
#     info_dict.append(({
#       "Atomic Number": el_row.atomic_no,
#       "Symbol": el_row.id,
#       "Name": el_row.name,
#       "Valency": el_row.valency,
#       "Group Number": el_row.group_no,
#       "Period Number": el_row.period_no,
#       "State(Room temp.)": el_row.state_rt
#     }))
#   return info_dict

# 