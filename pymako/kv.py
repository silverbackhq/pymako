"""
Consul KV Store Module
"""

from .client import Client
from urllib.parse import urlencode


class KV(Client):

    def __init__(self, consul_url, api_version="v1"):
        super().__init__(consul_url, api_version)

    def get(self, key, parameters={}, default=""):
        uri = self.build_uri("/kv/%s" % key, parameters)
        response = self.get_request(uri, {}, "")
        if response.status_code == Client.OK:
            return response.text
        else:
            return default

    def update(self, key, value, parameters={}):
        uri = self.build_uri("/kv/%s" % key, parameters)
        response = self.put_request(uri, {}, value)
        if response.status_code == Client.OK:
            return True
        else:
            return False

    def delete(self, key, parameters={}):
        uri = self.build_uri("/kv/%s" % key, parameters)
        response = self.delete_request(uri, {}, "")
        if response.status_code == Client.OK:
            return True
        else:
            return False

    def build_uri(self, uri, parameters={}):
        query = urlencode(parameters, doseq=True)
        if query != "":
            uri += "?%s" % (query)
        return uri
