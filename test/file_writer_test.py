import os
import unittest

from file_writer import *
from writer_test import *
from lower_case_converter_test import *
from upper_case_converter_test import *
from stupid_remover_test import *
from duplicate_remover_test import *
from combine_converter_test import *


class FileWriterTest(WriterTest, LowerCaseConverterTest, UpperCaseConverterTest,
                     StupidRemoverTest, DuplicateRemoverTest, CombineConverterTest, unittest.TestCase):
    def tearDown(self):
        if os.path.exists("FileWriter.txt"):
            os.remove("FileWriter.txt")

    def get_writer(self, converter):
        return FileWriter("FileWriter.txt", converter)

    def get_content(self, writer):
        open_file = open(writer.contents_file, "r")
        return open_file.read()
