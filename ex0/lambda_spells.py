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
        'max_power': lambda mages: max((mage['power'] for mage in mages)),
        'min_power': lambda mages: min(mage['power'] for mage in mages),
        'avg_power': lambda mages: round(sum(mages['power'])/len(mages), 2)
        }


if __name__ == "__main__":
    def main() -> None:
        print("Testing artifact sorter...")
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

        spells_join = lambda spells: "".join(spells)
        print("Testing spell transformer...")
        spells: 
        print(spells_join(spell_transformer(spells)))

    main()
