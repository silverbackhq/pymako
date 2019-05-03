import unittest


import requests
from pymako import Status
from unittest.mock import patch


class TestStatus(unittest.TestCase):

    status = None

    def setUp(self):
        self.status = Status("http://api.com")

    @patch('requests.get')
    def test_leader(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "[LEADER]"
        self.assertEqual("[LEADER]", self.status.leader())

    @patch('requests.get')
    def test_peers(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "[PEERS]"
        self.assertEqual("[PEERS]", self.status.peers())


if __name__ == "__main__":
    unittest.main()
