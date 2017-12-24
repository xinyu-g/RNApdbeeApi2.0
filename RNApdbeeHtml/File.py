import os


class File:

    def __init__(self, extension, file_content):
        self.extension = extension
        self.file_content = file_content

    def __str__(self):
        return self.file_content

    def save_file(self, absolute_path):
        self.valid_path(absolute_path)
        try:
            file = open(absolute_path, 'w')
            file.write(self.file_content)
        except IOError:
            raise Exception('Something went wrong while trying to write file!')
        finally:
            file.close()

    def valid_path(self, absolute_path):
        filename, file_extension = os.path.splitext(absolute_path)
        if file_extension[1:].upper() != self.extension.upper():
            raise ValueError('Wrong file extension! Should be {}'.format(file_extension[1:]))