from converter import *


class WriterTest():
    def test_write(self):
        writer = self.get_writer([Converter()])
        writer.write("123")
        self.assertEqual("123", self.get_content(writer))

    def test_write_two_string(self):
        writer = self.get_writer([Converter()])
        writer.write("123")
        writer.write(" Hello")
        self.assertEqual("123 Hello", self.get_content(writer))

    def test_write_three_string(self):
        writer = self.get_writer([Converter()])
        writer.write("123")
        writer.write("   ")
        writer.write("Test")
        self.assertEqual("123   Test", self.get_content(writer))

    def test_write_close(self):
        writer = self.get_writer([Converter()])
        writer.write("123")
        writer.close()
        self.assertEqual("123", self.get_content(writer))

    def test_write_close_write(self):
        writer = self.get_writer([Converter()])
        writer.write("123")
        writer.close()
        writer.write(" Hello")
        self.assertEqual("123", self.get_content(writer))

    def test_close_write(self):
        writer = self.get_writer([Converter()])
        writer.close()
        writer.write("123")
        self.assertEqual("", self.get_content(writer))
