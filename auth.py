import functools
from flask import (
    Blueprint, flash, g, render_template, request, url_for, session
)
from werkzeug.security import check_password_hash, generate_password_hash
from todo.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")