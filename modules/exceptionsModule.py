class ExceptionsModule(Exception):
    def __init__(self, value):
        print('Error: ', value)