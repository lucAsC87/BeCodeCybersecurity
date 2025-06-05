from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

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
		return redirect(url_for("home", name=name))


if __name__ == "__main__":
	app.run(debug=True)
