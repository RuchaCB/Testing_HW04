import unittest
from Arun_04a import getInfo


class TestGit(unittest.TestCase):
    """Class is used to test getInfo"""

    def test_getInfo(self):
        self.assertEqual([repo for repo in getInfo("NAruneshwar")], ([('810Assignment', 2), ('Testing', 12), ('Triangle', 9)]))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)