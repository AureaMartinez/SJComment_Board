from config import SQLALCHEMY_DATABASE_URI
from app import db, models
db.create_all()
