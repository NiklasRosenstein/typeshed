from urllib3.exceptions import HTTPError as BaseHTTPError

from .models import Request, Response

class RequestException(OSError):
    response: Response | None
    request: Request | None
    def __init__(self, *args: object, request: Request | None = ..., response: Response | None = ...) -> None: ...

class InvalidJSONError(RequestException): ...
class JSONDecodeError(InvalidJSONError): ...

class HTTPError(RequestException):
    request: Request
    response: Response
    def __init__(self, *args: object, request: Request, response: Response) -> None: ...

class ConnectionError(RequestException): ...
class ProxyError(ConnectionError): ...
class SSLError(ConnectionError): ...
class Timeout(RequestException): ...
class ConnectTimeout(ConnectionError, Timeout): ...
class ReadTimeout(Timeout): ...
class URLRequired(RequestException): ...
class TooManyRedirects(RequestException): ...
class MissingSchema(RequestException, ValueError): ...
class InvalidSchema(RequestException, ValueError): ...
class InvalidURL(RequestException, ValueError): ...
class InvalidHeader(RequestException, ValueError): ...
class InvalidProxyURL(InvalidURL): ...
class ChunkedEncodingError(RequestException): ...
class ContentDecodingError(RequestException, BaseHTTPError): ...
class StreamConsumedError(RequestException, TypeError): ...
class RetryError(RequestException): ...
class UnrewindableBodyError(RequestException): ...
class RequestsWarning(Warning): ...
class FileModeWarning(RequestsWarning, DeprecationWarning): ...
class RequestsDependencyWarning(RequestsWarning): ...
