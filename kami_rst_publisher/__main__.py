"""
"""  # TODO doc for main


PROGRAM_NAME = 'kami_rst_publisher'


from argparse import ArgumentParser, RawTextHelpFormatter, FileType
from sys import exit

from .cli_web_server import web_server_main, WEB_SERVER_DEFAULT_PORT



psr = ArgumentParser(prog=PROGRAM_NAME,
        description=__doc__, formatter_class=RawTextHelpFormatter)


# positional arguments
psr.add_argument('SOURCE',
        type=FileType('r', encoding='utf-8'),
        help='')  # TODO


# TODO DESTINATION


# options

psr.add_argument('-w', '--web-server',
        action='store',
        nargs='?',
        const=WEB_SERVER_DEFAULT_PORT,
        type=int,
        metavar='PORT',
        help='')  # TODO 

psr.add_argument('-p', '--render-preset',
        action='store',
        default='dark',
        type=str,
        choices=['dark', 'light'],
        help='')  # TODO

psr.add_argument('-l', '--light',
        action='store_true',
        help='equivalent to --preset light')




psr.add_argument('-v', '--verbose',
        action='count',
        default=0)

psr.add_argument('-q', '--quiet',
        action='count',
        default=0)



# TODO recursive mode
# TODO light mode
# TODO suffix
# TODO expression filter

# todo -d option to add date
# e.g. -d 13 means add .#[02022-03-05] as suffix

# todo eliminate the need write ``.. default-role:: smart`` for each file
# TODO allow .md file






if __name__ == "__main__":
    args = psr.parse_args()

    # convert args
    verbosity = args.verbose - args.quiet
    render_preset = args.light or args.render_preset

    if args.web_server:
        web_server_main(args.SOURCE, args.web_server, render_preset)


    exit(0)
