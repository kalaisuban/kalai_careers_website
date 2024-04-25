from flask import Flask, jsonify,render_template
from sample_answer import Sample
app=Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi, India',
    'salary': 'Rs. 15,00,000'
  }
]
# company_name="Kalai"
sam=Sample()
@app.route("/")
def hello_world():
  # return "Hello,This is kalaiking45"
  return render_template("home.html",temp=sam.get_output(),temp1=JOBS,company_name="Kalai")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True) 