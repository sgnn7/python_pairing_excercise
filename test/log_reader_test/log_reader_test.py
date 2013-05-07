import unittest
from mock import Mock, call
import os

from log_reader.log_reader import LogReader

class LogReaderTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_log_reader_exits_if_file_is_not_specified(self):
        self.assertFalse(True)
