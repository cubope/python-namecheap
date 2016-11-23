"""
ikcam
96365a97cf67403cba9afd10fd65e800
"""
from namecheap.resources import (
    Domains
)


class Namecheap(object):
    name = 'Namecheap'
    _response = None

    def __init__(
        self,
        API_ROOT='https://api.sandbox.namecheap.com/xml.response',
        API_USER='ikcam',
        API_KEY='96365a97cf67403cba9afd10fd65e800',
        DEFAULT_IP='179.7.140.94',
        *args,
        **kwargs
    ):
        self._API_ROOT = API_ROOT
        self._API_USER = API_USER
        self._API_KEY = API_KEY
        self._DEFAULT_IP = DEFAULT_IP

        self.domains = Domains(**self.credentials)

    @property
    def credentials(self):
        return {
            'API_ROOT': self._API_ROOT,
            'API_USER': self._API_USER,
            'API_KEY': self._API_KEY,
            'DEFAULT_IP': self._DEFAULT_IP
        }

    def __str__(self):
        return self.name
