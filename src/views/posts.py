"""
Handle posts
"""

from flask import Blueprint, request, jsonify

story_bp = Blueprint("posts", __name__)

story_bp.route("/api/story/create", methods=["POST"])
def create_story():
    """
    Create the new story
    """

    # Get data

