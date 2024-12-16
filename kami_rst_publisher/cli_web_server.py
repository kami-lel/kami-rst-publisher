"""
implement --web-server option of kami_rst_publisher CLI
"""


WEB_SERVER_DEFAULT_PORT = 8080


from http.server import HTTPServer, BaseHTTPRequestHandler

from docutils import io
from docutils.core import publish_programmatically

from .cli_utils import determine_parser, create_settings_overrides


def generate_html_content_on_http_request():
    global src_file_path
    global render_preset

    # BUG can not properly publish
    output, publisher = publish_programmatically(
        source_class=io.FileInput, source=None, source_path=src_file_path,
        destination_class=io.StringOutput,
                destination=None, destination_path=None,
        reader=None, reader_name='standalone',
        parser=None, parser_name=determine_parser(),
        writer=None, writer_name='html5',
        settings=None, settings_spec=None,
                settings_overrides=create_settings_overrides(render_preset),
        config_section=None, enable_exit_status=None)

    return output


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        html_content = generate_html_content_on_http_request()
        self.wfile.write(html_content)


def web_server_main(src_file_arg, port, render_preset_arg):
    global src_file_path
    global render_preset

    # create http server
    address = ('', port)
    httpd = HTTPServer(address, CustomHTTPRequestHandler)

    src_file_path = src_file_arg.name
    render_preset = render_preset_arg

    # run server
    try:
        httpd.serve_forever()
    finally:
        httpd.server_close()
