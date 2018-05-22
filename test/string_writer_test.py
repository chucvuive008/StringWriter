import unittest

from lower_case_converter_test import *
from writer_test import *
from string_writer import *
from upper_case_converter_test import *
from stupid_remover_test import *
from duplicate_remover_test import *
from combine_converter_test import *


class StringWriterTest(WriterTest, LowerCaseConverterTest, UpperCaseConverterTest, StupidRemoverTest,
                       DuplicateRemoverTest, CombineConverterTest, unittest.TestCase):
    def test_Canary(self):
        self.assertTrue(True)

    def get_writer(self, converter):
        return StringWriter(converter)

    def get_content(self, writer):
        return writer.contents



