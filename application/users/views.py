from application import app
from flask import render_template, request

@app.route("/users/register/")
def user_form():
    return render_template("users/register.html")

@app.route("/users/", methods=["POST"])
def users_create():
    print(request.form.get("username"))

    return "Rekisteroityminen onnistui?"
