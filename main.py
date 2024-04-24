from flask import Flask,render_template
from sample_answer import Sample
app=Flask(__name__)

sam=Sample()
@app.route("/")
def hello_world():
  # return "Hello,This is kalaiking45"
  return render_template("home.html",temp=sam.get_output())

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True) 