"""Biolevate SDK exceptions."""

from __future__ import annotations


class BiolevateError(Exception):
    """Base exception for all Biolevate SDK errors."""


class NotFoundError(BiolevateError):
    """Raised when a requested resource is not found."""


class AuthenticationError(BiolevateError):
    """Raised when authentication fails."""


class APIError(BiolevateError):
    """Raised when the API returns an unexpected error."""

    def __init__(self, status_code: int, message: str = "") -> None:
        self.status_code = status_code
        self.message = message
        super().__init__(f"API error {status_code}: {message}")
