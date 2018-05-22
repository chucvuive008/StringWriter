from writer import *


class StringWriter(Writer):
    def __init__(self, converters):
        super().__init__(converters)
        self.contents = ""

    def write_content(self, string):
        if self.open:
            self.contents += string
