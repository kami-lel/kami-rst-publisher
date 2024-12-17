"""personalized rST publisher based on docutils but with extra roles & directives

- single mode:
- recursive mode

- web server mode


help='like -b, but recursively into each sub-folder of SOURCE. '
'This flag overwrites -b. '
'DESTINATION is not used when -r')


"""  # TODO doc for main


PROGRAM_NAME = 'kami_rst_publisher'
FILE_ENCODING = 'utf-8'


from argparse import ArgumentParser, RawTextHelpFormatter, FileType
from sys import exit

from .cli_file import cli_single_mode_main, cli_recursive_mode_main
from .cli_web_server import \
        cli_web_server_mode_main, WEB_SERVER_DEFAULT_PORT



psr = ArgumentParser(prog=PROGRAM_NAME,
        description=__doc__, formatter_class=RawTextHelpFormatter)


# positional arguments
psr.add_argument('SOURCE',
        type=FileType('r', encoding=FILE_ENCODING),
        help='SOURCE of raw text, as file/directory path')
psr.add_argument('DESTINATION',
        nargs='?',
        type=FileType('w', encoding=FILE_ENCODING),
        help= \
"""DESTINATION for rendered files, as file/directory path;
if absent, rendered files will be saved alongside SOURCE""")


# options
psr.add_argument('-r', '--recursive',
        action='store_true',
        help='enable recursive mode, v.s.')

psr.add_argument('-w', '--web-server',
        action='store',
        nargs='?',
        const=WEB_SERVER_DEFAULT_PORT,
        type=int,
        metavar='PORT',
        help='enable web server mode, v.s.')

# TODO implement
psr.add_argument('-s', '--suffix',
        nargs='?',
        const='.R',
        help= 'append SUFFIX to rendered files; default to ".R"')

psr.add_argument('-p', '--render-preset',
        action='store',
        default='dark',
        type=str,
        choices=['dark', 'light'],
        help='set rendering presets')

psr.add_argument('-l', '--light',
        action='store_true',
        help='equivalent to --preset light')

psr.add_argument('-v', '--verbose',
        action='count',
        default=0)

psr.add_argument('-q', '--quiet',
        action='count',
        default=0)


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
        cli_web_server_mode_main(args.SOURCE, args.web_server, render_preset)
    elif args.recursive:
        cli_recursive_mode_main(args.SOURCE, args.DESTINATION,
                args.suffix, args.render_preset, verbosity)
    else:
        cli_single_mode_main(args.SOURCE, args.DESTINATION,
                args.suffix, args.render_preset, verbosity)

    exit(0)
