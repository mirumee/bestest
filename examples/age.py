import datetime

class AgeProtocol(object):
    '''
    Twice as clever! Not only using overkill math but also caching the result
    '''
    def __init__(self, birth_date):
        self.birth_date = birth_date

    @property
    def age(self):
        if not hasattr(self, '_age'):
            self._age = int((datetime.now().date() - self.birth_date).days / 365.2425)
        return self._age
