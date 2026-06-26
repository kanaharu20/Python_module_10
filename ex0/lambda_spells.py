#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifacts: artifacts['power'],
        reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(
        lambda mages: mages['power'] >= min_power, mages
    ))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(
        lambda spell: " * "+spell+" * ", spells
    ))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': (lambda m: max(mage['power'] for mage in m))(mages),
        'min_power': (lambda m: min(mage['power'] for mage in m))(mages),
        'avg_power': (lambda m: round(sum(mage['power'] for mage in m) / len(m), 2))(mages)
        }


if __name__ == "__main__":
    def main() -> None:
        print("\nTesting artifact sorter...")
        artifacts: list[dict] = [
            {"name": "orb", "type": "Crystal", "power": "85"},
            {"name": "stuff", "power": "92", "type": "Fire"}
            ]

        sorted_list = artifact_sorter(artifacts)

        ret_artifacts = lambda artifact: (
            f"{artifact['type']} {artifact['name']}"
            f" ({artifact['power']}power)"
            )
        print(
            f"{ret_artifacts(sorted_list[0])} comes "
            f"before {ret_artifacts(sorted_list[1])}"
            )
        for arti in sorted_list[2:]:
            print(f"{ret_artifacts(arti)}")

        print("\nTesting power filter...")
        mages: list[dict] = [
            {'name': "Alex", "power": 10, 'element': 'fire'},
            {'name': "Jordan", "power": 20, 'element': 'ice'},
            {'name': "Riley", "power": 30, 'element': 'lightning'},
            {'name': "Casey", "power": 40, 'element': 'earth'},
            {'name': "Morgan", "power": 50, 'element': 'wind'}
        ]
        for mage in power_filter(mages, 30):
            print(
                f"{mage['name']}: {mage['power']}, {mage['element']}",
                end="")

        print("\n\nTesting spell transformer...")
        spells: list[str] = ["fireball", "heal", "shield"]
        spells_join = lambda spells: "".join(spells)
        print(spells_join(spell_transformer(spells)))

        print("\nTesting mage_stats")
        stats: dict = mage_stats(mages)
        params: list[str] = ["max_power", "min_power", "avg_power"]
        for i in range(len(params)):
            print(f"{params[i]}: {stats[params[i]]}")

    main()
