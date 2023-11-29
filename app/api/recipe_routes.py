from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Recipe

recipe_routes = Blueprint('recipes', __name__)
