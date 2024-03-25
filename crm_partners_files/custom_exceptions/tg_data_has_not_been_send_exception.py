__all__ = ['TgSendDataError', ]


class TgSendDataError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'Telegram error: {self.message}'
        else:
            return 'Telegram error.'
