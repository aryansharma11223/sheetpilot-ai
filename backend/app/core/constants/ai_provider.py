"""
===============================================================================
SheetPilot AI

CORE-004 : AI Provider Constants
===============================================================================
"""

from enum import Enum


class AIProvider(str, Enum):
    """Supported AI providers."""

    OPENAI = "openai"
    GEMINI = "gemini"
    CLAUDE = "claude"
    OLLAMA = "ollama"
