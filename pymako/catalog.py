"""
Catalog
"""

from .client import Client


class Catalog(Client):

    def __init__(self, consul_url, api_version="v1"):
        super().__init__(consul_url, api_version)
