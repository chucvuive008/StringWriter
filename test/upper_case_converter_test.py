from upper_case_converter import *


class UpperCaseConverterTest:
    def test_upper_case_converter_write(self):
        writer = self.get_writer([UpperCaseConverter()])
        writer.write("hello")
        self.assertEqual("HELLO", self.get_content(writer))

    def test_upper_case_write_close_write(self):
        writer = self.get_writer([UpperCaseConverter()])
        writer.write("hello")
        writer.close()
        writer.write(" tom")
        self.assertEqual("HELLO", self.get_content(writer))

    def test_upper_case_two_write(self):
        writer = self.get_writer([UpperCaseConverter()])
        writer.write("hello")
        writer.write(" tom")
        self.assertEqual("HELLO TOM", self.get_content(writer))

    def test_upper_case_close_write(self):
        writer = self.get_writer([UpperCaseConverter()])
        writer.close()
        writer.write("hello")
        self.assertEqual("", self.get_content(writer))