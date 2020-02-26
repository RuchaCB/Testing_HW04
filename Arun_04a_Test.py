import unittest
import Arun_04a
from unittest import mock

class TestGit(unittest.TestCase):
    """Class is used to test getInfo"""
    @mock.patch("Arun_04a.getInfo")
    def test_getInfo(self, mock_get):
        mock_get.return_value = [('hellogitworld', 30), ('helloworld', 6), ('Mocks', 10), ('Project1', 2), ('threads-of-life', 1)]
        expected = [('hellogitworld', 30), ('helloworld', 6), ('Mocks', 10), ('Project1', 2), ('threads-of-life', 1)]
        git_id = "richkempinski"
        self.assertEqual(expected, Arun_04a.getInfo(git_id))

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
