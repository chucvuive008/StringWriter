from writer import *

class FileWriter(Writer):
    def __init__(self, file_name, converters):
        super().__init__(converters)
        self.contents_file = file_name

    def write_content(self, string):
        open_file = open(self.contents_file, "a")
        if self.open:
            open_file.write(string)

