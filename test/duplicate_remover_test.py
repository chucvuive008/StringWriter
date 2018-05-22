from duplicate_remover import *


class DuplicateRemoverTest:
    def test_duplicate_remover_write(self):
        writer = self.get_writer([DuplicateRemover()])
        writer.write("you are are my friend friend")
        self.assertEqual("you are my friend", self.get_content(writer))

    def test_duplicate_remover_two_write(self):
        writer = self.get_writer([DuplicateRemover()])
        writer.write("you are are my friend friend .")
        writer.write("my friend friend is nice")
        self.assertEqual("you are my friend .my friend is nice", self.get_content(writer))

    def test_duplicate_remover_write_close_write(self):
        writer = self.get_writer([DuplicateRemover()])
        writer.write("you are are my friend friend .")
        writer.close()
        writer.write("my friend friend is nice")
        self.assertEqual("you are my friend .", self.get_content(writer))