import unittest


import requests
from pymako import KV
from unittest.mock import patch


class TestKV(unittest.TestCase):

    kv = None

    def setUp(self):
        self.kv = KV("http://api.com")

    def test_build_uri(self):
        uri = self.kv.build_uri("/kv/key", {
            "dc": "us",
            "recurse": "true",
            "raw": "false"
        })
        self.assertEqual(uri, "/kv/key?dc=us&recurse=true&raw=false")

    @patch('requests.get')
    def test_get(self, mock_get):
        mock_get.return_value.status_code = 404
        self.assertEqual(self.kv.get("key", {}, "Default"), "Default")

    @patch('requests.get')
    def test_get_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'Value'
        self.assertEqual("Value", self.kv.get("key"))

    @patch('requests.get')
    def test_update_error(self, mock_get):
        mock_get.return_value.status_code = 500
        self.assertTrue(self.kv.update("key", "NewValue"))

    @patch('requests.get')
    def test_update_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'Value'
        self.assertTrue(self.kv.update("key", "NewValue"))

    @patch('requests.get')
    def test_delete_error(self, mock_get):
        mock_get.return_value.status_code = 500
        self.assertTrue(self.kv.delete("key"))

    @patch('requests.get')
    def test_delete_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'Value'
        self.assertTrue(self.kv.delete("key"))


if __name__ == "__main__":
    unittest.main()