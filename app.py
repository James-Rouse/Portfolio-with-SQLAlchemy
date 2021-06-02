from flask import render_template, url_for, request
from models import db, Project, app

@app.route("/")
def portolio_index():
    portfolio = Project.query.all()
    return render_template("index.html", portfolio=portfolio)

@app.route("/project/<id>")
def project_details():
    pass

@app.route("/project/new")
def new_project():
    pass

@app.route("/project/<id>/edit")
def edit_project():
    pass

@app.route("/delete/<id>")
def delete_project(id):
    pass


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8000, host="0.0.0.0")
