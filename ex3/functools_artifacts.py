#!/usr/bin/env python3

from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return reduce(operator.add, spells)
    elif operation == "multiply":
        return reduce(operator.mul, spells)
    elif operation == "max":
        return max(spells)
    elif operation == "min":
        return min(spells)
    else:
        print("Given operator is not supported.")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    heal = partial(base_enchantment, power=50, element="heal")
    fireball = partial(base_enchantment, power=50, element="fireball")
    iceball = partial(base_enchantment, power=50, element="iceball")
    return {"heal": heal, "fireball": fireball, "iceball": iceball}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n >= 2:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)
    else:
        raise ValueError("Index number can not be negative.")


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell_process(arg: Any) -> str:
        return "Unknown spell type"

    @spell_process.register(int)
    def int_process(arg: int) -> str:
        return f"{arg} damege"

    @spell_process.register(str)
    def str_process(arg: str) -> str:
        return arg

    @spell_process.register(list)
    def list_process(arg: list) -> str:
        return f"{len(arg)} spells"

    return spell_process


if __name__ == "__main__":
    def main() -> None:
        print("\nTesting spell reducer...")
        spells: list[int] = [40, 10, 20, 30]
        print(f"Sun: {spell_reducer(spells, "add")}")
        print(f"Product: {spell_reducer(spells, "multiply")}")
        print(f"Max: {spell_reducer(spells, "max")}")

        print()
        print("Testing memoized fibonacci...")
        print(f"Fib(0): {memoized_fibonacci(0)}")
        print(f"Fib(1): {memoized_fibonacci(1)}")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")

        print()
        print("Testing spell dispatcher...")
        ex_dispatcher = spell_dispatcher()
        print(f"Damage spell: {ex_dispatcher(42)}")
        print(f"Enchantment: {ex_dispatcher("fireball")}")
        spells_list: list[str] = ["fireball", "iceball", "heal"]
        print(f"Multi-cast: {ex_dispatcher(spells_list)}")
        print(f"{ex_dispatcher((1, 2))}")

    main()
