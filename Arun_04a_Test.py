import unittest
from Arun_04a import getInfo
from unittest import mock

@mock.patch("Arun_04a.getInfo")
class TestGit(unittest.TestCase):
    """Class is used to test getInfo"""
    
    def test_getInfo(self, mock_get):
        self.assertEqual([repo for repo in getInfo("richkempinski")], ([('hellogitworld', 30), ('helloworld', 6), ('Mocks', 10), ('Project1', 2), ('threads-of-life', 1)]))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)