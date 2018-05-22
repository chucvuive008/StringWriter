from converter import *


class UpperCaseConverter(Converter):
    def convert(self, string):
        return string.upper()