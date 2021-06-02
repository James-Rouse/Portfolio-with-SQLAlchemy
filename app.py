from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
db = SQLAlchemy(app)


engine = create_engine("sqlite:///portfolio.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Project(db.Model):
    """Model class for adding and editing project information."""

    __tablename__ = "project"

    id = Column("ID", Integer, primary_key=True)
    title = Column("Title", String)
    date = Column("Date", Date)
    description = Column("Description", String)
    skills_practiced = Column("Skills Practiced", String)
    github_repo = Column("GitHub Repo", String)


@app.route("/")
def portolio_index():
    total_portfolio = Project.query.all()
    return render_template("index.html", total_portfolio=total_portfolio)

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
    app.run(port=8000, host="0.0.0.0")
