"""
implment web server mode of kami_rst_publisher CLI
"""


WEB_SERVER_DEFAULT_PORT = 8080


from http.server import HTTPServer, BaseHTTPRequestHandler
import logging

from docutils.core import publish_string

from .cli_utils import PROGRAM_NAME, WRITER_NAME, \
        normalize_src_arg_and_test_access, \
        create_settings_overrides


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global logger
        global src_arg_cache
        global mlo_config_cache

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        src_path = normalize_src_arg_and_test_access(src_arg_cache)

        with open(src_path, 'r') as src_file:
            raw_content = src_file.read()

        result = publish_string(raw_content,
                parser_name= mlo_config_cache.get_parser_name(
                        src_path, src_arg_cache),
                writer_name=WRITER_NAME,
                settings_overrides=settings_overrides)

        logger.debug('render new page triggered by GET')

        self.wfile.write(result)


def cli_web_server_mode_main(src_arg, port, mlo_config, render_preset):
    global logger
    global src_arg_cache
    global settings_overrides
    global mlo_config_cache

    logger = logging.getLogger(PROGRAM_NAME)
    logger.debug('start: cli_web_server_mode_main')

    src_arg_cache = src_arg
    settings_overrides = create_settings_overrides(render_preset)
    mlo_config_cache = mlo_config

    # create http server
    address = ('', port)
    httpd = HTTPServer(address, CustomHTTPRequestHandler)

    # create url
    url = r'http://localhost:{}'.format(httpd.server_address[1])

    # run server
    try:
        print('Access rendered page by:\n\t{}'.format(url))
        httpd.serve_forever()

    # FIXME catch exception: OSError: [Errno 98] Address already in use
    finally:
        httpd.server_close()
        logger.debug('finish: cli_web_server_mode_main')
