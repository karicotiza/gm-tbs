"""Faction logic module."""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Faction:
    """Faction structure."""

    name: str
