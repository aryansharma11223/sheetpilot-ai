"""
===============================================================================
AEVON

Knowledge Category
===============================================================================
"""

from enum import Enum


class KnowledgeCategory(str, Enum):
    """
    Categories of knowledge documents.
    """

    GENERAL = "general"

    ARCHITECTURE = "architecture"
    DESIGN = "design"
    REQUIREMENTS = "requirements"
    STANDARDS = "standards"
    API = "api"
    GUIDE = "guide"
    TASK = "task"

    OTHER = "other"
