"""Peasant unit instance module."""

from src.instances.factions.heaven import heaven
from src.logic import creature

peasant: creature.Creature = creature.Creature(
    name='Peasant',
    stats=creature.Stats(
        attack=1,
        defense=1,
        hit_points=3,
        damage=creature.Damage(minimum=1, maximum=1),
        initiative=8,
        speed=4,
        shots=0,
        mana=0,
    ),
    information=creature.Information(
        faction=heaven,
        tier=creature.Tier.first,
        growth=22,
        cost=15,
        experience=15,
    ),
)
