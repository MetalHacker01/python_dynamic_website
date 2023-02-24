from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_SECRET']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    s = text("select * from jobs where id = :val")
    result = conn.execute(s, {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return (rows[0]._asdict())


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "insert into applications (job_id, FirstName, LastName, email, location, cv) values (:job_id, :FirstName, :LastName, :email, :location, :cv)"
    )
    result = conn.execute(
      query, {
        "job_id": job_id,
        "FirstName": data['firstName'],
        "LastName": data['lastName'],
        "email": data['email'],
        "location": data['region'],
        "cv": data['cv']
      })
