"""
Client
"""

import requests
from .exceptions import ConsulApiException
from urllib.parse import urlencode


class Client():

    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    __consul_url = None
    __api_version = "v1"

    def __init__(self, consul_url, api_version="v1"):
        self.__consul_url = consul_url
        self.__api_version = api_version

    def get_request(self, uri, headers, data):
        """Get Request"""
        url = "%(base_url)s/%(version)s/%(uri)s" % {
            "base_url": self.__consul_url.strip("/"),
            "version": self.__api_version,
            "uri": uri.strip("/")
        }
        try:
            request = requests.get(
                url,
                headers=headers,
                data=data
            )
            return request
        except Exception:
            raise ConsulApiException("Request Failure: status code %d response %s" % (request.status_code, request.text))

    def put_request(self, uri, headers, data):
        """Put Request"""
        url = "%(base_url)s/%(version)s/%(uri)s" % {
            "base_url": self.__consul_url.strip("/"),
            "version": self.__api_version,
            "uri": uri.strip("/")
        }
        try:
            request = requests.put(
                url,
                headers=headers,
                data=data
            )
            return request
        except Exception:
            raise ConsulApiException("Request Failure: status code %d response %s" % (request.status_code, request.text))

    def post_request(self, uri, headers, data):
        """Post Request"""
        url = "%(base_url)s/%(version)s/%(uri)s" % {
            "base_url": self.__consul_url.strip("/"),
            "version": self.__api_version,
            "uri": uri.strip("/")
        }
        try:
            request = requests.post(
                url,
                headers=headers,
                data=data
            )
            return request
        except Exception:
            raise ConsulApiException("Request Failure: status code %d response %s" % (request.status_code, request.text))

    def delete_request(self, uri, headers, data):
        """Delete Request"""
        url = "%(base_url)s/%(version)s/%(uri)s" % {
            "base_url": self.__consul_url.strip("/"),
            "version": self.__api_version,
            "uri": uri.strip("/")
        }
        try:
            request = requests.delete(
                url,
                headers=headers,
                data=data
            )
            return request
        except Exception:
            raise ConsulApiException("Request Failure: status code %d response %s" % (request.status_code, request.text))

    def build_uri(self, uri, parameters={}):
        query = urlencode(parameters)
        if query != "":
            uri += "?%s" % (query)
        return uri
