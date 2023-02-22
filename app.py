from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
  'id': 1,
  'title': 'Web Developer',
  "region": 'Europe',
  "salary": 'Starting from 5000$',
  'seniority': 'Junior',
  'working-hours': 'Part Time'
}, {
  'id': 2,
  'title': 'Data Analyst',
  'region': 'North America',
  'salary': 'Starting from 5500$',
  'seniority': 'Mid-Senior Level',
  'working-hours': 'Full Time'
}, {
  'id': 3,
  'title': 'Mkt Manager',
  'region': 'North America',
  'seniority': 'Field Expert',
  'working-hours': 'Full Time'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=jobs, company_name='Python')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
