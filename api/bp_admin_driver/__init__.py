from flask import Blueprint


BP_NAME = 'bp_admin_driver'
bp = Blueprint(BP_NAME, __name__)

from . import views
