from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "easiestjobapplicationever"


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

@app.route("/application-form")
def application_form():
	"""Present the form."""

	return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def application_received():
	"""Shows congratulatory message that user has been hired."""

	firstname = request.form.get('firstname')
	lastname = request.form.get('lastname')
	salary = request.form.get('salary')
	position = request.form.get('position')

	if salary.isdigit() == False:
		flash("Enter a number without symbols or commas.")
		return render_template("application-form.html")
	else:
		return render_template("application-response.html", firstname=firstname,
															lastname=lastname,
															salary=salary,
															position=position)

if __name__ == "__main__":
    app.run(debug=True)
