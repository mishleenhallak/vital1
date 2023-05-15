from flask import Flask, render_template, redirect, request, url_for

app = Flask (__name__)

@app.route("/")
def home():
  return render_template("home.html")
  
@app.route ("/start")
def start():
  return redirect(url_for('consent'))

@app.route('/consent', methods =["GET","POST"])
def consent() :
  if request.method == 'POST':
    if 'agree' in request.form:
      return redirect(url_for("input"))
    else:
      return render_template('consent.html', error='You must agree to proceed.')
  return render_template("consent.html")

@app.route("/input")
def input():
  #name = request.form['name']
  #age = request.form['age']
  #height = request.form['height']
  #weight = request.form["weight"]
  return render_template("input.html")

if __name__ == "__main__":
  app.run(host ="0.0.0.0", debug=True)

