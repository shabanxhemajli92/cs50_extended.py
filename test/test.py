import unittest
from student import get_student

class TestDeleteFile(unittest.TestCase):

    def test_get_student(self):
       self.assertEqual(("John"),"John")