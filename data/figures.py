import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase


class Figure(SqlAlchemyBase):
    __tablename__ = 'figures'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    images = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.VARCHAR, nullable=True)
