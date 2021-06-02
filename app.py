from flask import render_template, url_for, request, redirect
from models import db, Project, app

@app.route("/")
def portolio_index():
    """Homepage/index."""
    portfolio = Project.query.all()
    return render_template("index.html", portfolio=portfolio)

@app.route("/project/<id>")
def project_details():
    """Display details of a project."""
    return render_template("detail.html")

@app.route("/project/new")
def new_project():
    """Add a new project."""
    pass

@app.route("/project/<id>/edit")
def edit_project():
    """Edit a project."""
    pass

@app.route("/delete/<id>")
def delete_project(id):
    """Delete a project."""
    pass


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.1")
