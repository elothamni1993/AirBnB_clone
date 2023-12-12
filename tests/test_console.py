ting: console module'''

import unittest
from io import StringIO
import sys
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    '''Testing Console module'''

    def setUp(self):
        '''setUp function'''
        self.copy = sys.stdout
        self.cap = StringIO()
        sys.stdout = self.cap

    def tearDown(self):
        '''TearDown function'''
        sys.stdout = self.copy

    def create_console(self):
        '''Instantiate an object from the HBNBCommand class.'''
        return HBNBCommand()

    def test_quit_exists(self):
        '''Testing quit exists'''
        cnsl = self.create_console()
        self.assertTrue(cnsl.onecmd("quit"))

    def test_EOF_exists(self):
        '''Testing EOF exists'''
        cnsl = self.create_console()
        self.assertTrue(cnsl.onecmd("EOF"))

    def test_all_method(self):
        '''Testing all method'''
        cnsl = self.create_console()
        cnsl.onecmd("all")
        self.assertTrue(isinstance(self.cap.getvalue(), str))

    # Other test methods remain unchanged

if __name__ == '__main__':
    unittest.main()

