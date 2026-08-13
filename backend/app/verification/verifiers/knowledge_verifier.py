"""
===============================================================================
AEVON

Module:
    Knowledge Verifier

Purpose:
    Verifies the health of the Knowledge subsystem.
===============================================================================
"""

from __future__ import annotations

import time

from app.core.paths import paths
from app.knowledge import KnowledgeIndexer
from app.verification.contracts import (
    VerificationResult,
    VerificationStatus,
)

from .base_verifier import BaseVerifier


class KnowledgeVerifier(BaseVerifier):
    """
    Verifies the Knowledge subsystem.
    """

    @property
    def name(self) -> str:
        return "Knowledge"

    def run(self) -> VerificationResult:

        start = time.perf_counter()

        messages: list[str] = []
        errors: list[str] = []

        try:
            indexer = KnowledgeIndexer()
            messages.append("KnowledgeIndexer created.")

            messages.append(
                f"Registered Indexers: {indexer.indexer_count}"
            )

            repo = indexer.index_directory(paths.docs)

            messages.append(
                f"Knowledge Items Indexed: {repo.count}"
            )

            status = VerificationStatus.PASS

        except Exception as ex:
            status = VerificationStatus.FAIL
            errors.append(str(ex))

        duration = time.perf_counter() - start

        return VerificationResult(
            subsystem=self.name,
            status=status,
            duration_seconds=duration,
            messages=messages,
            errors=errors,
        )
