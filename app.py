"""An interface for a portfolio web application.

The main (index) page lists your projects including the project title and short
description. Each project links to a detail page that displays the title, date,
and description.

The application lets the user add or edit project information. When adding or
editing a project, the application prompts the user for title, date, skills,
description, and a link to a repo. The results for these entries are stored in
a database and displayed on the homepage.

"""
from flask import render_template, url_for, request, redirect
from models import db, Project, app
from datetime import datetime

@app.route("/")
def portfolio_index():
    """Portfolio homepage/index."""
    portfolio = Project.query.all()
    return render_template("index.html", portfolio=portfolio)

@app.route("/about")
def about_author():
    """Display author's about page."""
    return render_template("about.html")

@app.route("/#skill")
def skills_section():
    return render_template("index.html")

@app.route("/project/<id>")
def project_details(id):
    """Display details of a project."""
    project = Project.query.get(id)
    return render_template("detail.html", project=project)

@app.route("/project/new", methods=['GET', 'POST'])
def new_project():
    """Add a new project."""
    if request.form:
        split_date = request.form["date"].split("-")
        year = int(split_date[0])
        month = int(split_date[1])
        new_project = Project(title=request.form["title"],
                              date_completed=datetime.strptime(f'{year}-{month}', '%Y-%m').date(),
                              description=request.form["description"],
                              skills_practiced=request.form["skills"],
                              github_repo=request.form["github"])
        # https://stackoverflow.com/questions/34646025/specify-a-datetime-date-without-a-day-in-python
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("portfolio_index"))
    return render_template("projectform.html")

@app.route("/project/<id>/edit")
def edit_project():
    """Edit a project."""
    return render_template("projectform.html")

@app.route("/projects/<id>/delete")
def delete_project(id):
    """Delete a project."""
    pass


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.1")
