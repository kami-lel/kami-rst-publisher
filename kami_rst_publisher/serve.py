"""
"""  # TODO

# TODO mention this program in __main__

DEFAULT_HTTP_SERVE_PORT = 8080

PROGRAM_NAME = 'kami_rst_publisher.serve'



from argparse import ArgumentParser, RawTextHelpFormatter, FileType
from sys import exit
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import time
import logging # TODO use logging module


from watchdog.events import FileSystemEventHandler, LoggingEventHandler
from watchdog.observers.polling import PollingObserver

from .publish import publish_rst_file2html_str


class RawFileChangeHandler(FileSystemEventHandler):
    """event handler for catching file modification"""

    def __init__(self, httpd):
        super().__init__()
        self.httpd = httpd

    def on_created(self, event):
        global html_content_cache

        html_content_cache = '123'

        for conn in self.httpd.connections:
            conn.handler.update_page()

    def on_deleted(selve, event):
        if event.is_directory:
            print('on del')  # TODO handle


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.update_page()

    def update_page(self):
        global html_content_cache
        self.wfile.write(html_content_cache.encode('utf-8'))
        self.wfile.flush()




psr = ArgumentParser(prog=PROGRAM_NAME,
        description=__doc__,
        formatter_class=RawTextHelpFormatter)


# positional args
psr.add_argument('SOURCE',
        type=FileType('r', encoding='utf-8'),
        help='')  # TODO

psr.add_argument('PORT',
        nargs='?',
        default=DEFAULT_HTTP_SERVE_PORT,
        type=int,
        help='')  # TODO


# options
psr.add_argument('-p', '--preset',
        default='dark',
        type=str,
        choices=['dark', 'light'],
        help='set rendering preset, including stylesheets, etc.')

psr.add_argument('-l', '--light',
        action='store_true',
        help='equivalent to --preset light')

psr.add_argument('-v', '--verbose',
        action='count',
        default=0)

psr.add_argument('-q', '--quiet',
        action='count',
        default=0)


if __name__ == '__main__':
    args = psr.parse_args()

    # parse args
    verbosity = args.verbose - args.quiet
    src_path = args.SOURCE.name

    # TODO
    global html_content_cache
    html_content_cache = publish_rst_file2html_str()

    # create http server
    httpd = HTTPServer(('', args.PORT), CustomHTTPRequestHandler)

    # set up file monitoring
    observer = PollingObserver()
    observer.schedule(RawFileChangeHandler(httpd), src_path)
    observer.start()

    # run http server infinitely
    try:
        httpd.serve_forever()
    finally:
        pass

    # closes
    observer.stop()
    observer.join()
    httpd.server_close()

    exit(0)

