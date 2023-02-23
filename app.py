from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
  'id': 1,
  'img':
  "https://images.unsplash.com/photo-1618477388954-7852f32655ec?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8",
  'title': 'Web Developer',
  "region": 'Europe',
  "salary": 'Starting from 5000$',
  'seniority': 'Junior',
  'working-hours': 'Part Time'
}, {
  'id': 2,
  'img':
  "https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8",
  'title': 'Data Analyst',
  'region': 'North America',
  'salary': 'Starting from 5500$',
  'seniority': 'Mid-Senior Level',
  'working-hours': 'Full Time'
}, {
  'id': 3,
  'img':
  "https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8",
  'title': 'Mkt Manager',
  'region': 'North America',
  'seniority': 'Field Expert',
  'working-hours': 'Full Time'
}, {
  'id': 4,
  'img':
  "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8",
  'title': 'Marketing Coordinator',
  "region": 'North America',
  "salary": 'Starting from 4000$',
  'seniority': 'Entry Level',
  'working-hours': 'Part Time'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=jobs, company_name='Python')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
