from unittest import mock
from Arun_04a import getInfo


class TestGit(unittest.TestCase):
    """Class is used to test getInfo"""

    def test_getInfo(self):
        self.assertEqual([repo for repo in getInfo("richkempinski")], ([('hellogitworld', 30), ('helloworld', 6), ('Mocks', 10), ('Project1', 2), ('threads-of-life', 1)]))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)