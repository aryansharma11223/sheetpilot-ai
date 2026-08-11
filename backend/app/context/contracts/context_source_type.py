"""
===============================================================================
SheetPilot AI

Module:
    Context Source Type

Purpose:
    Defines the available context source types.
===============================================================================
"""

from __future__ import annotations

from enum import Enum


class ContextSourceType(str, Enum):
    """
    Types of context sources.
    """

    KNOWLEDGE = "knowledge"
    REPOSITORY = "repository"
    MEMORY = "memory"
    GIT = "git"
    CONVERSATION = "conversation"
