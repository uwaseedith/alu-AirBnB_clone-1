#!/usr/bin/python3
"""
Review class from base model.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class Docs"""
    place_id = ""
    user_id = ""
    text = ""