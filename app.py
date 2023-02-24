from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db
from mailjet_rest import Client
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='Python')


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route("/about")
def show_about():
  return render_template('about.html')


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return render_template('error.html', job=job)
  return render_template('jobpage.html', job=job)

def send_email(id, data): 
  data = request.form
  job = load_job_from_db(id)
  """
  This call sends a message to the given recipient with vars and custom vars.
  """
  api_key = os.environ['MJ_APIKEY_PUBLIC']
  api_secret = os.environ['MJ_APIKEY_PRIVATE']
  mailjet = Client(auth=(api_key, api_secret), version='v3.1')
  em_data = {
    'Messages': [
  		{
  			"From": {
  				"Email": "metalhacker01@gmail.com",
  				"Name": "Job_Application_Email"
  			},
  			"To": [
  				{
  					"Email": data['email'],
  					"Name": data['firstName']
  				}
  			],
  			"TemplateID": 4611439,
  			"TemplateLanguage": True,
  			"Subject": "Your job application for "+ job['title'] + " was received",
  			"Variables": {"title": job['title'],"firstName":data['firstName']}
  		}
  	]
  }
  result = mailjet.send.create(data=em_data)
  print (result.status_code)
  print (result.json())


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_job_from_db(id)
  add_application_to_db(id, data)
  send_email(id, data)
  return render_template('application_submit.html', application=data, job=job)






if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
