"""
===============================================================================

SheetPilot AI

Capability : CORE-002
Module     : Logger
Version    : 0.1.0
Status     : Development

Description
-----------
Centralized logging service used throughout SheetPilot.

===============================================================================
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from app.core.config import settings


_LOGGER_INITIALIZED = False


def _configure_logging() -> None:
    """
    Configure the global logging system.
    """

    global _LOGGER_INITIALIZED

    if _LOGGER_INITIALIZED:
        return

    from app.core.paths import paths

log_directory = paths.logs

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        log_directory / "sheetpilot.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper()),
        handlers=[console_handler, file_handler],
        force=True,
    )

    _LOGGER_INITIALIZED = True


def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger instance.

    Example
    -------
    logger = get_logger(__name__)
    """

    _configure_logging()

    return logging.getLogger(name)
