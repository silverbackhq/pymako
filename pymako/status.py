"""
Consul Cluster Status Module
"""

from .client import Client


class Status(Client):

    def __init__(self, consul_url, api_version="v1"):
        super().__init__(consul_url, api_version)

    def leader(self, parameters={}):
        uri = self.build_uri("/status/leader", parameters)
        response = self.get_request(uri, {}, "")
        if response.status_code == Client.OK:
            return response.text
        return ""

    def peers(self, parameters={}):
        uri = self.build_uri("/status/peers", parameters)
        response = self.get_request(uri, {}, "")
        if response.status_code == Client.OK:
            return response.text
        return ""
