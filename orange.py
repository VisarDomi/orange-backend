import os
from werkzeug.contrib.fixers import ProxyFix
from api import create_app
from api.common.database import db_session
from api.models.users import User, Admin, Driver, Employee, Secretary
from api.models.items import (
    Reservation,
    Company,
    Invoice,
    Item,
    Itinerary,
    ItineraryMaster,
    Stop,
)

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        "db_session": db_session,
        "User": User,
        "Admin": Admin,
        "Driver": Driver,
        "Employee": Employee,
        "Secretary": Secretary,
        "Company": Company,
        "Reservation": Reservation,
        "Invoice": Invoice,
        "Item": Item,
        "Itinerary": Itinerary,
        "ItineraryMaster": ItineraryMaster,
        "Stop": Stop,
    }


def run():
    # debug = os.environ.get('APP_DEBUG', True)
    host = os.environ.get("APP_HOST", "0.0.0.0")
    port = int(os.environ.get("APP_PORT", 8000))  # doesn't work, defaults to 5000

    # app.run(debug=debug, host=host, port=port)
    app.run(host=host, port=port)


wsgi = ProxyFix(app.wsgi_app)


if __name__ == "__main__":
    run()
