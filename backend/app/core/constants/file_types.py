"""
===============================================================================
AEVON

CORE-004 : File Type Constants
===============================================================================
"""

from enum import Enum


class FileType(str, Enum):
    """Supported file extensions."""

    PYTHON = ".py"
    MARKDOWN = ".md"
    JSON = ".json"
    YAML = ".yaml"
    CSV = ".csv"
    EXCEL = ".xlsx"
    PDF = ".pdf"
    TEXT = ".txt"
