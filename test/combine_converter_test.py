from stupid_remover import *
from upper_case_converter import *
from lower_case_converter import *
from duplicate_remover import *


class CombineConverterTest:
    def test_combine_upper_case_duplicate_remover(self):
        writer = self.get_writer([UpperCaseConverter(), DuplicateRemover()])
        writer.write("you are are my friend friend in high high school")
        self.assertEqual("YOU ARE MY FRIEND IN HIGH SCHOOL", self.get_content(writer))

    def test_combine_lower_case_duplicate_remover(self):
        writer = self.get_writer([LowerCaseConverter(), DuplicateRemover()])
        writer.write("YOU ARE ARE MY MY BEST FRIEND")
        self.assertEqual("you are my best friend", self.get_content(writer))

    def test_close_combine_upper_case_duplicate_remover(self):
        writer = self.get_writer([UpperCaseConverter(), DuplicateRemover()])
        writer.close()
        writer.write("you are are my friend friend in high high school")
        self.assertEqual("", self.get_content(writer))

    def test_close_combine_lower_case_duplicate_remover(self):
        writer = self.get_writer([LowerCaseConverter(), DuplicateRemover()])
        writer.close()
        writer.write("YOU ARE ARE MY MY BEST FRIEND")
        self.assertEqual("", self.get_content(writer))

    def test_combine_lower_case_stupid_remover(self):
        writer = self.get_writer([LowerCaseConverter(), StupidRemover()])
        writer.write("THE DRIVER IS SO STUPID")
        self.assertEqual("the driver is so s*****", self.get_content(writer))

    def test_close_combine_lower_case_stupid_remover(self):
        writer = self.get_writer([LowerCaseConverter(), StupidRemover()])
        writer.close()
        writer.write("THE DRIVER IS SO STUPID")
        self.assertEqual("", self.get_content(writer))

    def test_combine_stupid_remover_upper_case(self):
        writer = self.get_writer([StupidRemover(), UpperCaseConverter()])
        writer.write("The driver is stupid")
        self.assertEqual("THE DRIVER IS S*****", self.get_content(writer))

    def test_close_combine_stupid_remover_upper_case(self):
        writer = self.get_writer([StupidRemover(), UpperCaseConverter()])
        writer.close()
        writer.write("The driver is stupid")
        self.assertEqual("", self.get_content(writer))

    def test_combine_stupid_remover_duplicate_remover(self):
        writer = self.get_writer([StupidRemover(), DuplicateRemover()])
        writer.write("The driver is is so so stupid stupid")
        self.assertEqual("The driver is so s*****", self.get_content(writer))

    def test_close_combine_stupid_remover_duplicate_remover(self):
        writer = self.get_writer([StupidRemover(), DuplicateRemover()])
        writer.close()
        writer.write("The driver is is so so stupid stupid")
        self.assertEqual("", self.get_content(writer))

    def test_combine_lower_case_stupid_remover_duplicate_remover(self):
        writer = self.get_writer([LowerCaseConverter(), StupidRemover(), DuplicateRemover()])
        writer.write("ThE Driver IS iS so STUPID stupid")
        self.assertEqual("the driver is so s*****", self.get_content(writer))

    def test_combine_stupid_remover_upper_case_duplicate_remover(self):
        writer = self.get_writer([StupidRemover(), UpperCaseConverter(), DuplicateRemover()])
        writer.write("the driver is Is so stupid stupid")
        self.assertEqual("THE DRIVER IS SO S*****", self.get_content(writer))