class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file...")
        self.file = open(self.filename, self.mode, encoding="utf-8")
        return self.file          # value assigned to "as" variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file...")
        if self.file:
            self.file.close()
        # return False to re-raise exceptions, True to suppress
        return False


# usage
with FileManager("example.txt", "w") as f:
    f.write("Hello from context manager!")