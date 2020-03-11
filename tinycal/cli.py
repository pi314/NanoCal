"""
Define command line options
"""

from datetime import date
from argparse import ArgumentParser, RawTextHelpFormatter, ArgumentTypeError

from . import CALRCS
from . import __version__


parser = ArgumentParser(
    description='tinycal: A Python implementation of cal utility.',
    prog='tcal',
    epilog='Configuration files: {}'.format(CALRCS),
    formatter_class=RawTextHelpFormatter,
    )

parser.add_argument('--version', '-v', action='version', version=__version__)

parser.add_argument('--col', dest='col', default=None, type=int,
                    help='Specify the column numbers.')

parser.add_argument('-A', dest='after', default=None, type=int,
                    help='Display the number of months after the current month.')

parser.add_argument('-B', dest='before', default=None, type=int,
                    help='Display the number of months before the current month.')

parser.add_argument('-3', action='store_true', dest='a1b1', default=None,
                    help='Equals to -A 1 -B 1.')

parser.add_argument('-w', action='store_true', dest='wk', default=None,
                    help='Display week number.')
parser.add_argument('-W', action='store_false', dest='wk', default=None,
                    help='Don`t display week number.')

border_choices = ('full', 'basic', 'off', 'ascii', 'single', 'bold', 'double', 'weld', 'noweld')
def border_style_comma_separated_str(s):
    res = []
    for i in s.strip().split(','):
        if i in border_choices:
            res.append(i)
        else:
            raise ArgumentTypeError(
                    "invalid choice: '" + i + "'\n    (choose from " + repr(border_choices) + ")")

    return res

parser.add_argument('-b', '--border', type=border_style_comma_separated_str,
                    default=[], const='full', nargs='?',
                    help='Comma separated keywords to describe borders.\nValid keywords: '+ ','.join(border_choices))

parser.add_argument('-f', '--fill', action='store_true', dest='fill', default=None,
                    help='Fill every month into rectangle with previous/next month dates.')
parser.add_argument('-F', '--no-fill', action='store_false', dest='fill', default=None,
                    help='Don`t fill month into rectangle.')

parser.add_argument('--color', choices=['never', 'always', 'auto'], type=str,
                    default='auto', const='auto', nargs='?',
                    help='Enable/disable VT100 color output.')
parser.add_argument('-c', action='store_const', const='always', dest='color',
                    help='Enable VT100 color output, equals to --color=always')
parser.add_argument('-C', action='store_const', const='never', dest='color',
                    help='Disable VT100 color output, equals to --color=never')

parser.add_argument('-l', '--lang', choices=['jp', 'zh', 'en'], type=str,
                    help='Select the language used to display weekday.')

parser.add_argument('-j', action='store_const', const='jp', dest='lang',
                    help='Enable Japanese weekday names, equals to --lang=jp.')

parser.add_argument('-z', action='store_const', const='zh', dest='lang',
                    help='Enable Chinese weekday names, equals to --lang=zh.')

parser.add_argument('-e', action='store_const', const='en', dest='lang',
                    help='Enable Chinese weekday names, equals to --lang=en.')

parser.add_argument('-m', action='store_true', dest='start_monday', default=None,
                    help='Use Monday as first weekday.')
parser.add_argument('-M', action='store_false', dest='start_monday', default=None,
                    help='Use Sunday as first weekday.')

parser.add_argument('--cont', action='store_true', dest='cont', default=False,
                    help='Show the calendar in contiguous mode.')

def full_date_str(today_str):
    try:
        return date(*map(int, today_str.split('/')))
    except (TypeError, ValueError) as e:
        raise ArgumentTypeError("format should be yyyy/mm/dd")

parser.add_argument('--today', type=full_date_str, default=None,
                    help='Date that treated as today in format yyyy/mm/dd, used for debugging.')

parser.add_argument('year', type=int, nargs='?', default=None,
                    help='Year to display.')

parser.add_argument('month', type=int, nargs='?', default=None,
                    help='Month to display. Must specified after year.')
