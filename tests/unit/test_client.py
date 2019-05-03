import unittest

from pymako import Client


class TestClient(unittest.TestCase):

    def test_class(self):
        self.assertTrue(isinstance(Client("http://api.com"), Client))


if __name__ == "__main__":
    unittest.main()
