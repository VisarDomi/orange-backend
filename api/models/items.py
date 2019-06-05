from sqlalchemy import Table, Integer, String, Column, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..common.database import BaseModel
from ..common.serializers import ModelSerializerMixin


reservation_stop = Table(
    "reservation_stop",
    BaseModel.metadata,
    Column("reservation_id", Integer, ForeignKey("reservations.id")),
    Column("stop_id", Integer, ForeignKey("stops.id")),
)

employee_stop = Table(
    "employee_stop",
    BaseModel.metadata,
    Column("employee_id", Integer, ForeignKey("employees.id")),
    Column("stop_id", Integer, ForeignKey("stops.id")),
)


class Reservation(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    code = Column(String, default="no_code")
    destination = Column(String)
    date = Column(Date)
    time = Column(String)
    big_luggage = Column(String)
    small_luggage = Column(String)
    payment_method = Column(String)
    status = Column(String)

    company = relationship("Company", back_populates="reservations")
    company_id = Column(Integer, ForeignKey("companys.id"))

    driver = relationship("Driver", back_populates="reservations")
    driver_id = Column(Integer, ForeignKey("drivers.id"))

    # invoices
    invoices = relationship("Invoice", back_populates="reservation", lazy="dynamic")

    # stops
    stops = relationship(
        "Stop",
        secondary="reservation_stop",
        back_populates="reservations",
        lazy="dynamic",
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.code}, id = {self.id})"


class Invoice(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    ref = Column(String, default="no_ref")
    date = Column(Date)
    due = Column(Date)

    from_business_name = Column(String)
    from_addressline_1 = Column(String)
    from_addressline_2 = Column(String)
    from_city = Column(String)
    from_postcode = Column(String)
    from_vat = Column(String)
    from_phone = Column(String)

    to_client_name = Column(String)
    to_addressline_1 = Column(String)
    to_addressline_2 = Column(String)
    to_city = Column(String)
    to_postcode = Column(String)
    to_vat = Column(String)
    to_phone = Column(String)

    payment_account_name = Column(String)
    payment_account_sortcode = Column(String)
    payment_account_number = Column(String)

    invoice_notes = Column(Text)

    discount = Column(String)
    sub_total = Column(String)
    tax = Column(String)
    grand_total = Column(String)

    reservation = relationship("Reservation", back_populates="invoices")
    reservation_id = Column(Integer, ForeignKey("reservations.id"))

    # items
    items = relationship("Item", back_populates="invoice", lazy="dynamic")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.ref}, id = {self.id})"


class Item(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, default="no_name")
    date = Column(Date)
    description = Column(String)
    quantity = Column(String)
    price = Column(String)
    discount = Column(String)
    tax = Column(String)
    total = Column(String)

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

    company = relationship("Company", back_populates="itinerarys")
    company_id = Column(Integer, ForeignKey("companys.id"))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"


class ItineraryMaster(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, default="no_name")
    departure = Column(String)
    destination = Column(String)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"


class Stop(BaseModel, ModelSerializerMixin):

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, default="no_name")
    pickup = Column(String)

    # employees, reservations
    employees = relationship(
        "Employee",
        secondary="employee_stop",
        back_populates="stops",
        lazy="dynamic",
    )
    reservations = relationship(
        "Reservation",
        secondary="reservation_stop",
        back_populates="stops",
        lazy="dynamic",
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, id = {self.id})"
