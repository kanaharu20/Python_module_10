#!/usr/bin/env python3

from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        artifacts,
        key=lambda a: a['power'],
        reverse=True
        )


def power_filter(
        mages: list[dict[str, Any]], min_power: int) -> list[dict[str, Any]]:
    return list(filter(
        lambda m: m['power'] >= min_power, mages
    ))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(
        lambda spell: "* " + spell + " *", spells
    ))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        'max_power': (lambda m: max(mage['power'] for mage in m))(mages),
        'min_power': (lambda m: min(mage['power'] for mage in m))(mages),
        'avg_power': (lambda m: round(
            sum(mage['power'] for mage in m) / len(m), 2))(mages)
        }


if __name__ == "__main__":
    def main() -> None:
        print("\nTesting artifact sorter...")
        artifacts: list[dict[str, Any]] = [
            {"name": "orb", "type": "Crystal", "power": 85},
            {"name": "stuff", "power": 92, "type": "Fire"}
            ]

        sorted_list = artifact_sorter(artifacts)

        def ret_artifacts(artifact: dict[str, Any]) -> str:
            return (
                f"{artifact['type']} {artifact['name']}"
                f" ({artifact['power']} power)"
            )
        print(
            f"{ret_artifacts(sorted_list[0])} comes "
            f"before {ret_artifacts(sorted_list[1])}"
            )
        for arti in sorted_list[2:]:
            print(f"{ret_artifacts(arti)}")

        print("\nTesting power filter...")
        mages: list[dict[str, Any]] = [
            {'name': "Alex", "power": 10, 'element': 'fire'},
            {'name': "Jordan", "power": 20, 'element': 'ice'},
            {'name': "Riley", "power": 30, 'element': 'lightning'},
            {'name': "Casey", "power": 40, 'element': 'earth'},
            {'name': "Morgan", "power": 50, 'element': 'wind'}
        ]
        for mage in power_filter(mages, 30):
            print(f"{mage['name']}: {mage['power']}, {mage['element']}")

        print("\nTesting spell transformer...")
        spells: list[str] = ["fireball", "heal", "shield"]

        def ret_spells(s: list[str]) -> str:
            return " ".join(s)
        print(ret_spells(spell_transformer(spells)))

        print("\nTesting mage_stats")
        stats: dict[str, Any] = mage_stats(mages)
        params: list[str] = ["max_power", "min_power", "avg_power"]
        for i in range(len(params)):
            print(f"{params[i]}: {stats[params[i]]}")

    main()
