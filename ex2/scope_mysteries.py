#!/usr/bin/env python3

from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[..., Any]:
    count: int = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count
    return increment


def spell_accumulator(initial_power: int) -> Callable[..., Any]:
    total_power: int = initial_power

    def add_power(power_to_add: int) -> int:
        nonlocal total_power
        total_power += power_to_add
        return total_power
    return add_power


def enchantment_factory(enchantment_type: str) -> Callable[..., Any]:
    def enchant(enchantment_item: str) -> str:
        return f"{enchantment_type} {enchantment_item}"
    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        if key in memory:
            return memory[key]
        else:
            return "Memory not found"
    return {'recall': recall, 'store': store}


if __name__ == "__main__":
    def main() -> None:
        print("Testing mage counter...")
        cnt_call1 = mage_counter()
        for i in range(1, 3):
            print(f"counter_a call {i}: {cnt_call1()}")
        cnt_call2 = mage_counter()
        for i in range(1, 2):
            print(f"counter_b call {i}: {cnt_call2()}")
        print()

        print("Testing spell accumulator...")
        accml = spell_accumulator(100)
        print(f"Base 100, add 20: {accml(20)}")
        print(f"Base 100, add 30: {accml(30)}")
        print()

        print("Testing enchantment factory...")
        flaming = enchantment_factory("Flaming")
        frozen = enchantment_factory("Frozen")
        print(flaming("Sword"))
        print(frozen("Shield"))
        print()

        print("Testing memory vault...")
        mem_tool_dict = memory_vault()
        print("Store 'secret' = 42")
        mem_tool_dict['store']('secret', 42)
        print(f"Recall 'secret': {mem_tool_dict['recall']('secret')}")
        print(f"Recall 'unknown': {mem_tool_dict['recall']('unknown')}")

    main()
