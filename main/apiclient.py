import requests
import json


class APIClient(object):
    def __init__(self):
        """
        Initialize API client with application under test's base url and default header information
        """
        self.base_url = "http://localhost:5000"
        self.default_headers = {'content-type': 'application/json'}

    def get(self, uri, request_headers=None):
        """
        Perform http GET request for given uri, And use request header as per argument
        :param uri: <str> eg. "/login"
        :param request_headers: <dict> request headers dictionary eg. {'content-type': 'application/json'}
        :return: <dict> return reponse with keys "text" and "status_code"
        """
        if request_headers is None:
            request_headers = {}
        url = self.base_url + uri
        request_headers.update(self.default_headers)
        r = requests.get(url, headers=request_headers)
        response = {"text": json.loads(r.text), "status_code": r.status_code}
        return response

    def post(self, uri, request_payload, request_headers=None):
        """
        Perform http POST request for given uri, use request header as per argument and pass payload data to request
        :param uri: :param uri: <str> eg. "/favorite_restaurants"
        :param request_payload: {disct} payload dictionary eg. {"restaurant": name, "rating": rating}
        :param request_headers: <dict> request headers dictionary eg. {'content-type': 'application/json'}
        :return: <dict> return reponse with keys "text" and "status_code"
        """
        if request_headers is None:
            request_headers = {}
        url = self.base_url + uri
        request_headers.update(self.default_headers)
        r = requests.post(url, headers=request_headers, json=request_payload)
        response = {"text": json.loads(r.text), "status_code": r.status_code}
        return response

    def put(self, uri, request_payload, request_headers=None):
        """
        Perform http PUT request for given uri, use request header as per argument and pass payload data to request
        :param uri: :param uri: <str> eg. "/favorite_restaurants"
        :param request_payload: {disct} payload dictionary eg. {"restaurant": name, "rating": rating}
        :param request_headers: <dict> request headers dictionary eg. {'content-type': 'application/json'}
        :return: <dict> return reponse with keys "text" and "status_code"
        """
        if request_headers is None:
            request_headers = {}
        url = self.base_url + uri
        request_headers.update(self.default_headers)
        r = requests.put(url, headers=request_headers, json=request_payload)
        response = {"text": json.loads(r.text), "status_code": r.status_code}
        return response

    def delete(self, uri, request_payload=None, request_headers=None):
        """
        Perform http DELET request for given uri, use request header as per argument and pass payload data to request
        :param uri: :param uri: <str> eg. "/favorite_restaurants"
        :param request_payload: {disct} payload dictionary eg. {"restaurant": name, "rating": rating}
        :param request_headers: <dict> request headers dictionary eg. {'content-type': 'application/json'}
        :return: <dict> return reponse with keys "text" and "status_code"
        """
        if request_headers is None:
            request_headers = {}
        if request_payload is None:
            request_payload = {}
        url = self.base_url + uri
        request_headers.update(self.default_headers)
        r = requests.delete(url, headers=request_headers, json=request_payload)
        response = {"text": json.loads(r.text), "status_code": r.status_code}
        return response
