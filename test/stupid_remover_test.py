from stupid_remover import *


class StupidRemoverTest:
    def test_stupid_remover_write(self):
        writer = self.get_writer([StupidRemover()])
        writer.write("He is stupid stupid")
        self.assertEqual("He is s***** s*****", self.get_content(writer))

    def test_stupid_remover_write_close_write(self):
        writer = self.get_writer([StupidRemover()])
        writer.write("He is stupid")
        writer.close()
        writer.write("she is stupid")
        self.assertEqual("He is s*****", self.get_content(writer))

    def test_stupid_remover_two_write(self):
        writer = self.get_writer([StupidRemover()])
        writer.write("He is stupid. ")
        writer.write("She is stupid")
        self.assertEqual("He is s*****. She is s*****", self.get_content(writer))

