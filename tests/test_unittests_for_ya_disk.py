import unittest
from ya_disk import create_folder, tok, clearing_disk


class TestDisk(unittest.TestCase):

    def setUp(self):
        self.token = tok
        self.params = {'path': '||//'}
        self.params2 = {'pat': 'random folder'}

    def test_create_folder(self):
        self.assertEqual(201, create_folder(self.token))

    def test_create_folder2(self):
        self.assertEqual(409, create_folder(self.token))

    def test_create_folder3(self):
        self.assertEqual(401, create_folder('abcd'))

    def test_create_folder4(self):
        self.assertEqual(404, create_folder(self.token, self.params))

    def test_create_folder5(self):
        self.assertEqual(400, create_folder(self.token, self.params2))

    @classmethod
    def tearDownClass(cls):
        clearing_disk()
