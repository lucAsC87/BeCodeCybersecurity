from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:cisneros87@localhost/names'

db = SQLAlchemy(app)

class Name(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)

with app.app_context():
	db.create_all()

@app.route("/")
def home():
	name = request.args.get("name")
	if name:
		return f"Hello, {name}!"
	return "Hello, World!"

@app.route("/form", methods=["GET", "POST"])
def form():
	if request.method == "GET":
		return render_template("form.html")
	if request.method == "POST":
		name = request.form.get("name")
		new_name = Name(name=name)
		db.session.add(new_name)
		db.session.commit()
		return redirect(url_for("home", name=name))

@app.route("/names")
def names():
	list_names = Name.query.all()
	return render_template("names.html", names=list_names)


if __name__ == "__main__":
	app.run(debug=True)
