__all__ = ['GoogleSheetsTableNamingException', ]


class GoogleSheetsTableNamingException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'Google sheets table naming error: {self.message}'
        else:
            return 'Google sheets table naming error.'
