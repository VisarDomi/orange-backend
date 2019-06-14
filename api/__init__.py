from flask import Flask
from .common.middleware import (
    after_request_middleware,
    before_request_middleware,
    teardown_appcontext_middleware,
)
from .common.middleware import response
from .bp_dataintegration import bp as dataintegration_bp
from .bp_auth import bp as auth_bp
from .bp_admin import bp as admin_bp
from .bp_driver import bp as driver_bp
from .bp_invoice import bp as invoice_bp
from .bp_company import bp as company_bp
from .bp_employee import bp as employee_bp
from .bp_secretary import bp as secretary_bp
from .bp_reservation import bp as reservation_bp
from .bp_itinerary import bp as itinerary_bp
from .bp_itinerary_master import bp as itinerary_master_bp
import os
from config import Config
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler


def create_app(config_class=Config):

    # initialize flask application
    app = Flask(__name__)

    # config app
    app.config.from_object(config_class)

    # register all blueprints
    app.register_blueprint(dataintegration_bp, url_prefix="/api/dataintegration")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(driver_bp, url_prefix="/api/driver")
    app.register_blueprint(invoice_bp, url_prefix="/api/admin/reservation/<reservation_id>/invoice")
    app.register_blueprint(company_bp, url_prefix="/api/company")
    app.register_blueprint(employee_bp, url_prefix="/api/company/<company_id>/employee")
    app.register_blueprint(secretary_bp, url_prefix="/api/company/<company_id>/secretary")
    app.register_blueprint(reservation_bp, url_prefix="/api/company/<company_id>/reservation")
    app.register_blueprint(itinerary_bp, url_prefix="/api/company/<company_id>/itinerary")
    app.register_blueprint(itinerary_master_bp, url_prefix="/api/itinerary_master")

    # register custom response class
    app.response_class = response.JSONResponse

    # register before request middleware
    before_request_middleware(app=app)

    # register after request middleware
    after_request_middleware(app=app)

    # register after app context teardown middleware
    teardown_appcontext_middleware(app=app)

    # register custom error handler
    response.json_error_handler(app=app)

    # Logging
    is_app_debug = app.debug
    is_app_testing = app.testing

    if not is_app_debug and not is_app_testing:
        if app.config["MAIL_SERVER"]:
            auth = None
            if app.config["MAIL_USERNAME"] or app.config["MAIL_PASSWORD"]:
                auth = (app.config["MAIL_USERNAME"], app.config["MAIL_PASSWORD"])
            secure = None
            if app.config["MAIL_USE_TLS"]:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config["MAIL_SERVER"], app.config["MAIL_PORT"]),
                fromaddr=app.config["MAIL_USERNAME"],
                toaddrs=app.config["ADMINS"],
                subject="Orange-Network Failure",
                credentials=auth,
                secure=secure,
            )
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)
        if not os.path.exists("logs"):
            os.mkdir("logs")
        file_handler = RotatingFileHandler(
            "logs/orange-network.log", maxBytes=10240, backupCount=10
        )
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
            )
        )
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info("Orange-Network")

    return app
