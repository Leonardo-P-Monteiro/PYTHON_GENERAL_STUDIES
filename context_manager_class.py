# TRABALHANDO COM CONTEXT MANAGERS.
class MyOpen:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None
    
    def __enter__(self):
        print('Open the file.')
        self._file = open(self.file_path, 'w')
        return self._file

    def __exit__(self):
        print('Closed the file.')
        if self._file:
            self._file.close()

instance_ = MyOpen('file_exemple_context_maneger.txt', 'w')

with instance_ as file:
    file.write('Line 1\n')
    file.write("I'm practice the context manager knowledge.\n")
    file.write('Line 3\n')
