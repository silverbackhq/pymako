"""
Consul Cluster Status Module
"""

from .client import Client


class Status(Client):

    def __init__(self):
        super().__init__()
