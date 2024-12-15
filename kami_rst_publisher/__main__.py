
from argparse import ArgumentParser
from time import sleep
from datetime import datetime

from . import smart_role  # perform an import to init publisher
from .rst2html_file import Rst2htmlFile, Rst2htmlFileBatch, Rst2htmlFileRecursive


parser = ArgumentParser(
    prog='(kami rST publisher)publisher-cli.py',
    description='personalized rST publisher based on docutils but with extra roles & directives'
)


# positional arg
parser.add_argument('SOURCE',
                    help='SOURCE of rST text, file or directory path')
parser.add_argument('DESTINATION',
                    help='DESTINATION of rendered .html file(s), file or directory path. '
                         'Rendered file will be saved alongside with SOURCE if not given',
                    nargs='?')
# option
parser.add_argument('-b', '--batch',
                    action='store_true',
                    help='render any file with name fullmatching (regex) EXPRESSION in a directory SOURCE. '
                         'SOURCE & DESTINATION should be directory path. '
                         r'EXPRESSION default to ".+\.rst", but can be set by -f')
parser.add_argument('-r', '--recursive',
                    action='store_true',
                    help='like -b, but recursively into each sub-folder of SOURCE. '
                         'This flag overwrites -b. '
                         'DESTINATION is not used when -r')
parser.add_argument('-c', '--continuous',
                    const=5.0,
                    help='render all changed files once every WAIT seconds. WAIT default to 5.0.',
                    metavar='WAIT',
                    nargs='?',
                    type=float)
parser.add_argument('-l', '--light',
                    action='store_true',
                    help='render in light mode')
parser.add_argument('-v', '--verbose',
                    action='store_true')
parser.add_argument('-s', '--suffix',
                    const='.R',
                    help='SUFFIX for rendered file. Default to ".R"',
                    nargs='?')
parser.add_argument('-e', '--expression',
                    action='store',
                    help=r'with -b or -r, set EXPRESSION for file matching. Default to ".+\.rst"')
# todo -d option to add date
# e.g. -d 13 means add .#[02022-03-05] as suffix

# todo eliminate the need write ``.. default-role:: smart`` for each file
# TODO allow .md file
# TODO serve by server
# FIXME rm batch & continuous option


if __name__ == "__main__":
    args = parser.parse_args()

    # set dark/light mode
    lightmode = bool(args.light)

    # determine suffix
    suffix = '' if args.suffix is None else args.suffix

    # init
    if args.recursive:
        obj = Rst2htmlFileRecursive(args.SOURCE, args.expression, suffix, lightmode)
    elif args.batch:
        obj = Rst2htmlFileBatch(args.SOURCE, args.DESTINATION, args.expression, suffix, lightmode)
    else:
        obj = Rst2htmlFile(args.SOURCE, args.DESTINATION, suffix, lightmode)

    if args.verbose:
        print("[{}]".format(datetime.today().isoformat()))
        print(str(obj))

    while True:
        obj.render()

        if args.verbose and str(obj):
            print("[{}]".format(datetime.today().isoformat()))
            print(str(obj))

        if not args.continuous:
            # one-time render when not in repeat mode
            break

        sleep(args.continuous)
