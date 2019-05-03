"""
Consul Cluster Status Module
"""

from .client import Client
from urllib.parse import urlencode


class Status(Client):

    def __init__(self, consul_url, api_version="v1"):
        super().__init__(consul_url, api_version)

    def leader(self, parameters):
        uri = self.build_uri("/status/leader", parameters)
        response = self.get_request(uri, {}, "")
        if response.status_code == Client.OK:
            return response.text
        return ""

    def peers(self, parameters):
        uri = self.build_uri("/status/peers", parameters)
        response = self.get_request(uri, {}, "")
        if response.status_code == Client.OK:
            return response.text
        return ""

    def build_uri(self, uri, parameters={}):
        query = urlencode(parameters)
        if query != "":
            uri += "?%s" % (query)
        return uri
