"""."""

from flask_sqlalchemy_lite import SQLAlchemy
from sqlmodel import Session

DB = SQLAlchemy(session_options={"class_": Session})
