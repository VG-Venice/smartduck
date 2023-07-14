from sqlalchemy import create_engine, text

engine = create_engine(
"mysql+pymysql://kzmc8l01gcqm76fonj0a:pscale_pw_swThZwdpWhNpupKIqZJdO8njUX2Dfiy1zaa39NmCwWp@aws.connect.psdb.cloud/smartduck?charset=utf8mb4",
  connect_args={"ssl": {
    "ssl_ca": "cert.pem"
  }})

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

def load_element_from_db(atomic_no):
  with engine.connect() as conn:
    info = conn.execute(text(f"SELECT * FROM jobs WHERE id ={atomic_no}"))
    rows = []
    for el_row in info.all():
      rows.append(({  
      "Atomic Number": el_row.atomic_no,
      "Symbol": el_row.id,
      "Name": el_row.name,
      "Valency": el_row.valency,
      "Group Number": el_row.group_no,
      "Period Number": el_row.period_no,
      "State(Room temp.)": el_row.state_rt
      }))
    if len(rows) == 0:
      return None
    else:
      return el_row