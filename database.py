from sqlalchemy import create_engine, text
import os

# database: smartduck
# username: mwa1g3fkgfc8jt4l9bmu
# host: aws.connect.psdb.cloud
# password: pscale_pw_R7hzkuBcIi23wJ0tAYmHLE8nbwYnWfYdJK3E7vpVd30

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
      pTable[pr.posRow][pr.posCol] = str(pr.atomic_no) + '-' + pr.id + '-' + pr.name + '-' + pr.eType + '-'+ str(pr.valency)
  return pTable


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

# def load_element_from_db(atomic_no):
#   with engine.connect() as conn:
#     info = conn.execute(text(f"SELECT * FROM jobs WHERE id ={atomic_no}"))
#     rows = []
#     for el_row in info.all():
#       rows.append(({
#       "Atomic Number": el_row.atomic_no,
#       "Symbol": el_row.id,
#       "Name": el_row.name,
#       "Valency": el_row.valency,
#       "Group Number": el_row.group_no,
#       "Period Number": el_row.period_no,
#       "State(Room temp.)": el_row.state_rt
#       }))
#     if len(rows) == 0:
#       return None
#     else:
#       return el_row
