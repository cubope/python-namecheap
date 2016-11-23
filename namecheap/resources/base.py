import requests
from bs4 import BeautifulSoup
from lxml import objectify


class ResponseInstance(object):
    _name = 'ResponseInstance'

    def __str__(self):
        return '%s' % self._name


class Response(object):
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

    @property
    def credentials(self):
        return {
            'ApiUser': self._API_USER,
            'ApiKey': self._API_KEY,
            'UserName': self._API_USER,
            'ClientIp': self._DEFAULT_IP,
        }

    def _request(self, command, placeholder, args=None, is_list=False):
        kwargs = self.credentials

        kwargs.update({
            'Command': str(command),
        })

        if args:
            kwargs.update(args)

        print kwargs

        r = requests.get(
            url=self._API_ROOT,
            data=kwargs
        )

        self._response = r.content
        self._parse_response()

        if self._response_status() == 'ERROR':
            raise Exception(self._read_errors())

        return self.content(
            placeholder=placeholder
        )

    def _parse_response(self):
        if not isinstance(self._response, BeautifulSoup):
            self._response = BeautifulSoup(
                self._response, 'xml'
            )

    def content(self, placeholder):
        xml = self._response.find(placeholder)

        return objectify.fromstring(str(xml))

    def _response_status(self):
        if not self._response:
            raise Exception('No content.')

        return self._response.find('ApiResponse').attrs['Status']

    def _read_errors(self):
        if not self._response:
            raise Exception('No content.')

        return self._response.find('Errors').text.strip('\r\n')
