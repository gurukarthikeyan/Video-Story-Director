"""
Video Story Director

Build Entry Point
"""

import argparse
import sys

from builder.assembler import Assembler
from builder.reporter import Reporter
from builder.validator import Validator
from builder.utils import write_text
from builder.constants import RELEASES_DIR
from builder.config import (
    VERSION,
    BACKEND,
    OUTPUT_TEMPLATE,
)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Video Story Director Build Tool"
    )

    parser.add_argument(
        "--backend",
        default=BACKEND,
        help="Backend to build (ltx, wan, veo...)"
    )

    parser.add_argument(
        "--version",
        default=VERSION,
        help="Release version"
    )

    return parser.parse_args()


def main():

    args = parse_arguments()

    validator = Validator(args.backend)

    result = validator.validate()

    Reporter.print_validation(result)

    if not result.valid:
        return 1

    assembler = Assembler(
        backend=args.backend,
        version=args.version
    )

    prompt = assembler.build()

    output_file = (
        RELEASES_DIR /
        OUTPUT_TEMPLATE.format(
            backend=args.backend.upper(),
            version=args.version
        )
    )

    write_text(output_file, prompt)

    Reporter.print_build_summary(
        args.version,
        args.backend,
        output_file,
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())