import base64
import os
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from sqlalchemy import (
    Integer,
    String,
    Boolean,
    DateTime,
    Column,
    Date,
    Text,
    ForeignKey,
    Table,
)
from sqlalchemy.orm import relationship
from ..common.database import BaseModel
from ..common.serializers import ModelSerializerMixin


user_trip = Table(
    "user_trip",
    BaseModel.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("trip_id", Integer, ForeignKey("trips.id")),
)


class User(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    # database only
    password_hash = Column(String)
    role = Column(String, default="normal_user")

    # on create or login
    token = Column(String, unique=True)
    token_expiration = Column(DateTime)

    # dates
    register_date = Column(DateTime, default=datetime.utcnow)

    # intro
    full_name = Column(String, default="no_name")
    email = Column(String, unique=True)
    phone = Column(String)
    birthdate = Column(Date)
    bio = Column(Text)
    verified_id = Column(Boolean)
    verified_email = Column(Boolean)

    # photo
    photo_url = Column(String)
    photo_name = Column(String)

    # activity
    is_active = Column(Boolean)
    last_active = Column(DateTime)

    # one to many (should be one to one, car <-> owner)
    cars = relationship("Car", back_populates="owner", lazy="dynamic")

    driver_trips = relationship("Trip", back_populates="driver", lazy="dynamic")

    # many to many (for passengers)
    trips = relationship(
        "Trip", secondary="user_trip", back_populates="users", lazy="dynamic"
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode("utf-8")
        self.token_expiration = now + timedelta(seconds=expires_in)
        self.save()
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

    def __repr__(self):
        return f"{self.__class__.__name__}({self.full_name}, id = {self.id})"


class Car(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    make = Column(String, default="no_make")
    model = Column(String)
    color = Column(String)
    capacity = Column(String)

    # photo
    photo_url = Column(String)
    photo_name = Column(String)

    # many to one
    owner = relationship("User", back_populates="cars")
    owner_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.make}, id = {self.id})"


class Trip(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    start_place = Column(String, default="no_start_place")
    end_place = Column(String)
    start_datetime = Column(String)
    return_datetime = Column(String)
    price = Column(String)
    seats_available = Column(String)
    description = Column(String)
    is_done = Column(Boolean)

    # many to one
    driver = relationship("User", back_populates="driver_trips")
    driver_id = Column(Integer, ForeignKey("users.id"))

    # many to many
    users = relationship(
        "User", secondary="user_trip", back_populates="trips", lazy="dynamic"
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.start_place}, id = {self.id})"
