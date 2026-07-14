"""
Video Story Director
Build Reporter

Displays the results of the build process.
"""

from pathlib import Path

from builder.validator import ValidationResult


class Reporter:
    """
    Reports validation and build results.
    """

    @staticmethod
    def print_validation(result: ValidationResult) -> None:
        """
        Print validation results.
        """

        print("\n========================================")
        print("Repository Validation")
        print("========================================")

        if result.valid:
            print("[ OK ] Repository validation passed.")
        else:
            print("[FAIL] Repository validation failed.")

        if result.warnings:
            print("\nWarnings:")
            for warning in result.warnings:
                print(f"  - {warning}")

        if result.errors:
            print("\nErrors:")
            for error in result.errors:
                print(f"  - {error}")

    # ---------------------------------------------------------------------

    @staticmethod
    def print_build_summary(
        version: str,
        backend: str,
        output_file: Path,
    ) -> None:
        """
        Print build summary.
        """

        print("\n========================================")
        print("Video Story Director Build")
        print("========================================")

        print(f"Version : {version}")
        print(f"Backend : {backend.upper()}")

        print("\nOutput:")
        print(f"  {output_file}")

        print("\n[ OK ] Build completed successfully.")