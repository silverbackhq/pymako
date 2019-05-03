import unittest

from pymako import KV


class TestKV(unittest.TestCase):

    def test_class(self):
        self.assertTrue(isinstance(KV("http://api.com"), KV))


if __name__ == "__main__":
    unittest.main()
