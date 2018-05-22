class Writer:
    def __init__(self, converters):
        self.open = True
        self.converters = converters

    def write(self, string):
        for converter in self.converters:
            string = converter.convert(string)
        self.write_content(string)

    def close(self):
        self.open = False