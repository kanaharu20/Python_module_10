#!/usr/bin/env python3

from typing import Callable


def mage_counter() -> Callable:
    count: int = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count
    return increment


def spell_accumulator(initial_power: int) -> Callable:
    total_power: int = initial_power

    def add_power(power_to_add: int) -> int:
        nonlocal total_power
        total_power += power_to_add
        return total_power
    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(enchantment_item: str) -> str:
        return f"{enchantment_type} {enchantment_item}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, str] = {}

    def store(key, value) -> None:
        memory[key] = value

    def recall(key) -> str:
        if key in memory:
            return memory[key]
        else:
            return "Memory not found"
    return {'recall': recall, 'store': store}


if __name__ == "__main__":
    def main() -> None:
        print("Testing mage counter...")
        cnt_call1 = mage_counter()
        for i in range(5):
            print(f"cnt_call1 call{i}: {cnt_call1()}")
        cnt_call2 = mage_counter()
        for i in range(3):
            print(f"cnt_call2 call{i}: {cnt_call2()}")
        print()

        print("Testing spell accumulator...")
        accml = spell_accumulator(100)
        print(f"Base 100, add 20: {accml(20)}")
        print(f"Base 100, add 30: {accml(30)}")
        print()

        print("Testing enchantment factory...")
        flaming = enchantment_factory("Flaming")
        flozen = enchantment_factory("Flozen")
        print(flaming("Sword"))
        print(flozen("Shield"))
        print()

        print("Testing memory vault...")
        mem_tool_dict = memory_vault()
        print("Store 'secret' = 42")
        mem_tool_dict['store']('secret', 42)
        print(f"Recall 'secret': {mem_tool_dict['recall']('secret')}")
        print(f"Recall 'unknown': {mem_tool_dict['recall']('unknown')}")

    main()
