"""personalized rST publisher based on docutils but with extra roles & directives

Rendered file will be saved alongside with SOURCE if not given

"""

# TODO better doc
# TODO batch mode
# TODO recursive mode
# TODO continous mode
# TODO light option
# TODO verbose option
# TODO suffix option
# TODO expression filter
# TODO support .md
# TODO support http server

# todo eliminate the need write ``.. default-role:: smart`` for each file



PROGRAM_NAME = 'kami_rst_publisher'



from argparse import ArgumentParser, RawTextHelpFormatter
from sys import exit



psr = ArgumentParser(prog=PROGRAM_NAME,
        description=__doc__, formatter_class=RawTextHelpFormatter)


# positional arguments
psr.add_argument('SOURCE',
        help='SOURCE of markup text, file or directory path')
psr.add_argument('DESTINATION',
        nargs='?',
        help='DESTINATION of rendered .html file(s), file or directory path')


# options



# todo -d option to add date, e.g. -d 13 means add .#[02022-03-05] as suffix




def cli_main():
    args = psr.parse_args()

    pass  # TODO

    exit(0)

