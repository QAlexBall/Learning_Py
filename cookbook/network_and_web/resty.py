# resty.py
import cgi


def notfound_404(environ, start_response):
    start_response('404 Not Found', [('Content-type', 'text/plain')])
    return [b'Not Found']


class PathDispatcher:
    def __init__(self):
        self.path_map = {}

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
