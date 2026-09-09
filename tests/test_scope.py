import unittest
from app.scope import normalize_host

class ScopeTests(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize_host("HTTPS://Example.com/path"), "example.com")
    def test_reject(self):
        with self.assertRaises(ValueError): normalize_host("not a host")

if __name__ == "__main__": unittest.main()
