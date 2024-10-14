"""Unit logic module."""

from dataclasses import dataclass

from src.logic.faction import Faction
from src.logic.tier import Tier


@dataclass(slots=True, frozen=True)
class Damage:
    """Damage structure."""

    minimum: int
    maximum: int


@dataclass(slots=True, frozen=True)
class Stats:
    """Stats structure."""

    attack: int
    defense: int
    hit_points: int
    damage: Damage
    initiative: int
    speed: int
    shots: int
    mana: int


@dataclass(slots=True, frozen=True)
class Information:
    """Information structure."""

    faction: Faction
    tier: Tier
    growth: int
    cost: int
    experience: int


@dataclass(slots=True, frozen=True)
class Creature:
    """Creature structure."""

    name: str
    stats: Stats
    information: Information
