class Closer(open):
    '''A context manager to automatically close an object with a close method
    in a with statement.'''

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

    def __enter__(self, *args, **kwargs):
        return super().__enter( *args, **kwargs)

    def __exit__(self, exception_type, exception_val, trace):
        try:
            self.obj.close()
        except AttributeError: # obj isn't closable
            print('Not closable.')
            return True # exception handled successfully


with Closer('file.txt', 'r') as f:
    f.write('salam')