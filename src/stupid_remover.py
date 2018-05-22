from converter import *


class StupidRemover(Converter):
    def convert(self, string):
        return string.replace(" stupid", " s*****")

