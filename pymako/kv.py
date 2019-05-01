"""
Consul KV Store Module
"""

from .client import Client


class KV(Client):

    def __init__(self):
        super().__init__()
