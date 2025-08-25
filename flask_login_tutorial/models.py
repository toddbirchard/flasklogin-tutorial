"""Database models."""

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db


class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = "flasklogin-users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    website = db.Column(db.String(100), nullable=True)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    last_login = db.Column(db.DateTime)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User id={self.id}, name={self.name}, email={self.email}>"
