#!/usr/bin/env python3

from collections.abc import Callable
from typing import Any


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} then deal {power} damage"


def iceball(target: str, power: int) -> str:
    return f"Iceball hits {target} then deal {power} damage"


def spell_combiner(
        spell1: Callable[..., Any],
        spell2: Callable[..., Any]) -> Callable[..., Any]:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(
        base_spell: Callable[..., Any],
        multiplier: int) -> Callable[..., Any]:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(
        condition: Callable[..., Any],
        spell: Callable[..., Any]) -> Callable[..., Any]:
    return lambda target, power: (
        spell(target, power) if condition(target, power) else "Spell fizzled"
    )


def spell_sequence(spells: list[Callable[..., Any]]) -> Callable[..., Any]:
    return lambda target, power: [spell(target, power) for spell in spells]


if __name__ == "__main__":
    def main() -> None:
        print()
        print("Testing spell combiner...")
        print("Combined spell result: ", end="")
        print(spell_combiner(fireball, heal)("Dragon", 10))
        print()
        print("Testing power amplifier...")
        print("Power amplifier result: ", end="")
        print(power_amplifier(fireball, 3)("Dragon", 10))
        print()
        print("Testing conditional caster...")
        print("Fizzle: ", end="")
        print(conditional_caster(lambda _, p: p > 20, fireball)("Dragon", 10))
        print("Cast:   ", end="")
        print(conditional_caster(lambda _, p: p > 5, fireball)("Dragon", 10))
        print()
        print("Testing spell sequence...")
        print("Spell sequence result: ", end="")
        spells_list: list[Callable[..., Any]] = [fireball, iceball, heal]
        print(spell_sequence(spells_list)("Dragon", 10))

    main()
