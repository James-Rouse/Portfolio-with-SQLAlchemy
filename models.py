from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
db = SQLAlchemy(app)


class Project(db.Model):
    """Model class for adding and editing project information."""

    __tablename__ = "project"

    project_id = db.Column("ID", db.Integer, primary_key=True)
    project_title = db.Column("Title", db.String)
    date_completed = db.Column("Date", db.Date)
    project_description = db.Column("Description", db.String)
    skills_practiced = db.Column("Skills Practiced", db.String)
    github_repo = db.Column("GitHub Repo", db.String)

    def __repr__(self):
        """Return printable representation of Project."""
        return f"""\n----------
                \rProject ID: {self.project_id}
                \r----------
                \Project Title: {self.project_title}
                \r----------
                \Date Completed: {self.date_completed}
                \r----------
                \Description: {self.project_description}
                \r----------
                \Skills practiced: {self.skills_practiced}
                \r----------
                \rGithub Repo: {self.github_repo}
                \r----------\n"""
