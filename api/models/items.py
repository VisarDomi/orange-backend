from datetime import datetime
from sqlalchemy import Integer, String, Column, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..common.database import BaseModel
from ..common.serializers import ModelSerializerMixin


class Company(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, default="no_name")
    payment_frequency = Column(String)
    code = Column(String)
    invoice_number = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)

    # employees, secretary, reservations, itinerarys
    employees = relationship("Employee", back_populates="company", lazy="dynamic")
    secretarys = relationship("Secretary", back_populates="company", lazy="dynamic")
    reservations = relationship("Reservation", back_populates="company", lazy="dynamic")
    itinerarys = relationship("Itinerary", back_populates="company", lazy="dynamic")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"


class Reservation(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, default="no_name")
    destination = Column(String)
    date = Column(Date)
    time = Column(String)
    big_luggage = Column(String)
    small_luggage = Column(String)
    payment_method = Column(String)
    status = Column(String)
    vehicle_type = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)

    secretary = relationship("Secretary", back_populates="reservations")
    secretary_id = Column(Integer, ForeignKey("secretarys.id"))

    company = relationship("Company", back_populates="reservations")
    company_id = Column(Integer, ForeignKey("companys.id"))

    driver = relationship("Driver", back_populates="reservations")
    driver_id = Column(Integer, ForeignKey("drivers.id"))

    # invoices
    invoices = relationship("Invoice", back_populates="reservation", lazy="dynamic")

    # stops
    stops = relationship("Stop", back_populates="reservation", lazy="dynamic")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"


class Stop(BaseModel, ModelSerializerMixin):
    """Intermediate table employee-reservation"""

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, default="no_name")
    pickup = Column(String)
    time = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)

    # employee, reservation
    employee = relationship("Employee", back_populates="stops")
    employee_id = Column(Integer, ForeignKey("employees.id"))

    reservation = relationship("Reservation", back_populates="stops")
    reservation_id = Column(Integer, ForeignKey("reservations.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"


class Invoice(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    ref = Column(String, default="no_ref")
    datum = Column(Date)
    rechnung_nr = Column(String)
    uid_nr = Column(String)
    bank_name = Column(String)
    bic = Column(String)
    iban = Column(String)
    an_name = Column(String)
    an_company = Column(String)
    an_company_address = Column(String)
    an_company_postcode = Column(String)
    an_company_city = Column(String)
    an_company_state = Column(String)
    rechnungsersteller = Column(String)
    zahlungsform = Column(String)
    rechnung_datum = Column(Date)
    zahlungsziel = Column(String)
    tax = Column(String)
    total = Column(String)

    reservation = relationship("Reservation", back_populates="invoices")
    reservation_id = Column(Integer, ForeignKey("reservations.id"))

    timestamp = Column(DateTime, default=datetime.utcnow)

    # items
    items = relationship("Item", back_populates="invoice", lazy="dynamic")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.ref}, id = {self.id})"


class Item(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, default="no_name")
    pickup_date = Column(Date)
    pickup_address = Column(String)
    kst = Column(String)
    orderer_name = Column(String)
    message = Column(String)
    n_stops = Column(String)
    destination = Column(String)
    price = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)

    invoice = relationship("Invoice", back_populates="items")
    invoice_id = Column(Integer, ForeignKey("invoices.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"


class Itinerary(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, default="no_name")
    departure = Column(String)
    destination = Column(String)
    price = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)

    company = relationship("Company", back_populates="itinerarys")
    company_id = Column(Integer, ForeignKey("companys.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"


class ItineraryMaster(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, default="no_name")
    departure = Column(String)
    destination = Column(String)

    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"
