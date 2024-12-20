"""personalized rST publisher based on docutils but with extra roles & directives

- single mode: given a SOURCE file, publish a HTML file
- recursive mode: recusrively publish all files in SOURCE folder
- web server mode: given a SOURCE file, start a local web server to show it
"""

# todo -d option to add date
# e.g. -d 13 means add .#[02022-03-05] as suffix


import logging

VERBOSITY2LOGGING_LEVEL = {
        -1: logging.CRITICAL + 1,  # -q
        0: logging.WARNING,
        1: logging.INFO,  # -v
        2: logging.DEBUG}  # -vv


from argparse import ArgumentParser, RawTextHelpFormatter
import logging
from sys import exit

from .cli_single import cli_single_mode_main
from .cli_recursive import cli_recursive_mode_main, DEFAULT_FILTER
from .cli_web_server import \
        cli_web_server_mode_main, WEB_SERVER_DEFAULT_PORT
from .cli_utils import PRESETS, CustomizedLogHandler, PROGRAM_NAME


psr = ArgumentParser(prog=PROGRAM_NAME,
        description=__doc__, formatter_class=RawTextHelpFormatter)


# positional arguments
psr.add_argument('SOURCE',
        type=str,
        help='SOURCE of raw text, as file/directory path')
psr.add_argument('DESTINATION',
        nargs='?',
        type=str,
        help= \
"""DESTINATION for rendered files, as file/directory path
if absent, rendered files will be saved alongside SOURCE""")


# options
psr.add_argument('-r', '--recursive',
        action='store_true',
        help='enable recursive mode, v.s.')

# todo should work with .rst and .md
psr.add_argument('-e', '--expression',
        action='store',
        default=DEFAULT_FILTER,
        type=str,
        metavar='FILTER',
        help= \
r'''with --recursive, use FILTER to select files to be rendered
default to ".+\.rst"''')

psr.add_argument('-w', '--web-server',
        action='store',
        nargs='?',
        const=WEB_SERVER_DEFAULT_PORT,
        type=int,
        metavar='PORT',
        help='enable web server mode, v.s.')

psr.add_argument('-s', '--suffix',
        nargs='?',
        default='',
        const='.R',
        type=str,
        help= \
'''append SUFFIX to rendered files
default to ".R"
ignored in single mode and DESTINATION is given''')

psr.add_argument('-p', '--render-preset',
        action='store',
        default='light',
        type=str,
        choices=PRESETS,
        help='set rendering presets')

psr.add_argument('-D', '--dark',
        action='store_const',
        const='dark',
        help='equivalent to --preset dark')

psr.add_argument('-v', '--verbose',
        action='count',
        default=0)

psr.add_argument('-q', '--quiet',
        action='count',
        default=0)


if __name__ == "__main__":
    args = psr.parse_args()

    # convert args
    render_preset = args.dark or args.render_preset

    # set up logger
    logger = logging.getLogger(PROGRAM_NAME)
    verbosity = min(max(args.verbose - args.quiet, -1), 2)
    logger.setLevel(VERBOSITY2LOGGING_LEVEL[verbosity])
    logger.addHandler(CustomizedLogHandler())

    if args.web_server:
        cli_web_server_mode_main(args.SOURCE, args.web_server, render_preset)
    elif args.recursive:
        cli_recursive_mode_main(args.SOURCE, args.DESTINATION, args.expression,
                args.suffix, render_preset)
    else:
        cli_single_mode_main(args.SOURCE, args.DESTINATION,
                args.suffix, render_preset)

    exit(0)
