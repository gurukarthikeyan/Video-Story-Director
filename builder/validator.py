"""
Video Story Director
Repository Validator

Validates the repository structure before the build process begins.
"""

from dataclasses import dataclass, field

from builder.constants import (
    PROMPT_DIR,
    BACKENDS_DIR,
    RELEASES_DIR,
    PROMPT_MODULES,
)


# ============================================================================
# Validation Result
# ============================================================================

@dataclass
class ValidationResult:
    valid: bool = True
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


# ============================================================================
# Validator
# ============================================================================

class Validator:
    """
    Validates the repository structure before a build begins.
    """

    def __init__(self, backend: str):
        self.backend = backend

    def validate(self) -> ValidationResult:
        """
        Perform all repository validation checks.
        """

        result = ValidationResult()

        self._validate_directories(result)
        self._validate_prompt_modules(result)
        self._validate_backend(result)

        if result.errors:
            result.valid = False

        return result

    # ---------------------------------------------------------------------

    def _validate_directories(self, result: ValidationResult) -> None:
        """
        Verify required directories exist.
        """

        required = [
            PROMPT_DIR,
            BACKENDS_DIR,
            RELEASES_DIR,
        ]

        for directory in required:
            if not directory.exists():
                result.errors.append(
                    f"Missing directory: {directory}"
                )

    # ---------------------------------------------------------------------

    def _validate_prompt_modules(self, result: ValidationResult) -> None:
        """
        Verify every required prompt module exists and is not empty.
        """

        for module in PROMPT_MODULES:

            file_path = PROMPT_DIR / module

            if not file_path.exists():
                result.errors.append(
                    f"Missing prompt module: {module}"
                )
                continue

            if file_path.stat().st_size == 0:
                result.errors.append(
                    f"Empty prompt module: {module}"
                )

    # ---------------------------------------------------------------------

    def _validate_backend(self, result: ValidationResult) -> None:
        """
        Verify the selected backend exists and is not empty.
        """

        backend_file = (
            BACKENDS_DIR
            / self.backend
            / "backend.md"
        )

        if not backend_file.exists():
            result.errors.append(
                f"Backend not found: {self.backend}"
            )
            return

        if backend_file.stat().st_size == 0:
            result.errors.append(
                f"Backend is empty: {self.backend}"
            )