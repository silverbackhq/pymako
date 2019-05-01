"""
Catalog
"""

from .client import Client


class Catalog(Client):

    def __init__(self):
        super().__init__()
