class File:

    def __init__(self, extension, file_content):
        self.extension = extension
        self.file_content = file_content

    def __str__(self):
        return self.file_content

    def save_file(self, path):
        try:
            file = open(path, 'w')
            file.write(self.file_content)
        except IOError:
            raise Exception('Something went wrong while trying to write file!')
        finally:
            file.close()
