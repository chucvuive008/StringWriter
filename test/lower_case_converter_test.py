from lower_case_converter import *


class LowerCaseConverterTest:
    def test_lower_case_write(self):
        writer = self.get_writer([LowerCaseConverter()])
        writer.write("Hello")
        self.assertEqual("hello", self.get_content(writer))

    def test_lower_case_write_close_write(self):
        writer = self.get_writer([LowerCaseConverter()])
        writer.write("Hello")
        writer.close()
        writer.write("123")
        self.assertEqual("hello", self.get_content(writer))

    def test_lower_case_two_write(self):
        writer = self.get_writer([LowerCaseConverter()])
        writer.write("HELLO")
        writer.write(" Tom")
        self.assertEqual("hello tom", self.get_content(writer))

    def test_lower_case_close_write(self):
        writer = self.get_writer([LowerCaseConverter()])
        writer.close()
        writer.write("Hello")
        self.assertEqual("", self.get_content(writer))