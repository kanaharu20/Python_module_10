#!/usr/bin/env python3
from typing import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} then deal {power} damage"


def iceball(target: str, power: int) -> str:
    return f"Iceball hits {target} then deal {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda target, power: base_spell(target, power*multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda target, power: spell(
        target,
        power) if condition else "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda target, power: [spell(target, power) for spell in spells]


if __name__ == "__main__":
    def main() -> None:
        print()
        print("Testing spell_combiner...")
        print("Combined spell rerult: ", end="")
        print(spell_combiner(fireball, heal)("Dragon", 10))
        print()
        print("Testing power amplifier...")
        print("Combined spell rerult: ", end="")
        print(power_amplifier(fireball, 3)("Dragon", 10))
        print()
        print("Testing conditional caster...")
        print("Conditional caster rerult: ", end="")
        print(conditional_caster(False, fireball)("Dragon", 10))
        print()
        print("Testing spell sequence...")
        print("Spell sequence rerult: ", end="")
        spells_list: list[Callable] = [fireball, iceball, heal]
        print(spell_sequence(spells_list)("Dragon", 10))

    main()
