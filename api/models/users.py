import base64
import os
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..common.database import BaseModel
from ..common.serializers import ModelSerializerMixin


class User(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    email = Column(String, unique=True)

    timestamp = Column(DateTime, default=datetime.utcnow)

    # database only
    password_hash = Column(String)

    # on create or login
    token = Column(String, unique=True)
    token_expiration = Column(DateTime)

    # activity
    register_date = Column(DateTime, default=datetime.utcnow)

    # admin, driver, employee, company
    admin = relationship("Admin", uselist=False, back_populates="user")
    driver = relationship("Driver", uselist=False, back_populates="user")
    employee = relationship("Employee", uselist=False, back_populates="user")
    company = relationship("Company", uselist=False, back_populates="user")

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
        return f"{self.__class__.__name__}({self.email}, id = {self.id})"


class Admin(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    full_name = Column(String, default="no_full_name")

    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="admin")
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.full_name}, id = {self.id})"


class Driver(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    full_name = Column(String, default="no_full_name")
    status = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="driver")
    user_id = Column(Integer, ForeignKey("users.id"))

    # reservations
    reservations = relationship("Reservation", back_populates="driver", lazy="dynamic")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.full_name}, id = {self.id})"


class Company(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    full_name = Column(String, default="no_full_name")
    payment_frequency = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="company")
    user_id = Column(Integer, ForeignKey("users.id"))

    # employees, reservations, itinerarys
    employees = relationship("Employee", back_populates="company", lazy="dynamic")
    reservations = relationship("Reservation", back_populates="company", lazy="dynamic")
    itinerarys = relationship("Itinerary", back_populates="company", lazy="dynamic")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.full_name}, id = {self.id})"


class Employee(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    full_name = Column(String, default="no_full_name")
    address = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="employee")
    user_id = Column(Integer, ForeignKey("users.id"))

    company = relationship("Company", back_populates="employees")
    company_id = Column(Integer, ForeignKey("companys.id"))

    # stops
    stops = relationship("Stop", back_populates="employee", lazy="dynamic")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.full_name}, id = {self.id})"
