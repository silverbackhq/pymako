"""
Client
"""

import requests
from .exceptions import ConsulApiException


class Client():

    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204

    def get(self, url, headers, data):
        """Get Request"""
        try:
            request = requests.get(
                url,
                headers=headers,
                data=data
            )
            if request.status_code == Client.OK:
                return request.text
            else:
                raise ConsulApiException("Request Failure: status code %d response %s" % (request.status_code, request.text))
        except Exception:
            raise ConsulApiException("Request Failure: status code %d response %s" % (request.status_code, request.text))

    def put(self, url, headers, data):
        """Put Request"""
        try:
            request = requests.get(
                url,
                headers=headers,
                data=data
            )
            if request.status_code == Client.ACCEPTED:
                return request.text
            else:
                raise ConsulApiException("Request Failure: status code %d response %s" % (request.status_code, request.text))
        except Exception:
            raise ConsulApiException("Request Failure: status code %d response %s" % (request.status_code, request.text))

    def post(self, url, headers, data):
        """Post Request"""
        try:
            request = requests.get(
                url,
                headers=headers,
                data=data
            )
            if request.status_code == Client.CREATED:
                return request.text
            else:
                raise ConsulApiException("Request Failure: status code %d response %s" % (request.status_code, request.text))
        except Exception:
            raise ConsulApiException("Request Failure: status code %d response %s" % (request.status_code, request.text))

    def delete(self, url, headers, data):
        """Delete Request"""
        try:
            request = requests.get(
                url,
                headers=headers,
                data=data
            )
            if request.status_code == Client.NO_CONTENT:
                return request.text
            else:
                raise ConsulApiException("Request Failure: status code %d response %s" % (request.status_code, request.text))
        except Exception:
            raise ConsulApiException("Request Failure: status code %d response %s" % (request.status_code, request.text))
