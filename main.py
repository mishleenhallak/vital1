from flask import Flask, render_template, request

app = Flask (__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/input", methods=['GET', 'POST'])
def second_page():
  if request.method == 'POST':
    name = request.form['name']
    age = request.form['age']
    height = request.form['height']
    weight = request.form["weight"]
  return render_template("input.html")

if __name__ == "__main__":
  app.run(host ="0.0.0.0", debug=True)
