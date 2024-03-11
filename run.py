import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("secret_key_name")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", can_be_anything="About", company = data)


@app.route("/about/<member_name>")
def about_member(member_name):
    memberlist = {}
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                memberlist = obj
    return render_template("member.html", member = memberlist)


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have got your message".format(request.form.get("name")))
        # print(request.form)
        # print(request.form["name"])
    return render_template("contact.html", can_be_anything="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", can_be_anything="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)