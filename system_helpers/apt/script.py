import argparse
import logging
import pathlib

import typeguard

from system_helpers.apt.install import install_packages

@typeguard.typechecked
def parse_args() -> argparse.Namespace:
    """
    Parse CLI arguments.
    """
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(required = True)

    parser_ip = subparsers.add_parser('install-packages')

    parser_ip.add_argument('--clean',   action = 'store_true')
    parser_ip.add_argument('--update',  action = 'store_true')
    parser_ip.add_argument('--upgrade', action = 'store_true')

    parser_ip.add_argument(
        '--packages',
        help = "List of packages to install.",
        nargs = '*',
        required = False,
        dest = 'packages',
    )

    parser_ip.add_argument(
        '--requirement',
        help = 'Requirement file à la pip.',
        dest = 'requirements',
        action = 'append',
        type = pathlib.Path,
        required = False,
    )

    parser_ip.set_defaults(func = install_packages)

    return parser.parse_args()

@typeguard.typechecked
def main() -> None:

    logging.basicConfig(level=logging.INFO)

    args = parse_args()

    kwargs = vars(args)

    func = kwargs.pop('func')

    func(**kwargs)

if __name__ == "__main__":

    main()
