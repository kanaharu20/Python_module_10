#!/usr/bin/env python3

from collections.abc import Callable
from typing import Any
from functools import wraps
import time
import random


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        ret = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return ret
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if args[-1] >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def retry(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for cnt_try in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {cnt_try}/{max_attempts})")
                    if cnt_try == max_attempts:
                        return (
                            f"Spell casting failed after"
                            f" {max_attempts} attempts")
        return wrapper
    return retry


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and name.replace(" ", "").isalpha():
            return True
        else:
            return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"

    @staticmethod
    @spell_timer
    def fireball() -> None:
        time.sleep(0.1)
        print("Result: Fireball cast!")

    @staticmethod
    @retry_spell(3)
    def waaaaaaagh() -> str:
        i: int = random.randint(0, 9)
        if i % 3 == 0:
            return "Waaaaaaagh spelled !"
        else:
            raise Exception


if __name__ == "__main__":
    def main() -> None:
        mg = MageGuild()
        print("Testing spell timer...")
        mg.fireball()

        print()
        print("Testing retrying spell...")
        print(mg.waaaaaaagh())

        print()
        print("Testing MageGuild...")
        if mg.validate_mage_name("Alex"):
            print("True")
        else:
            print("False")
        if mg.validate_mage_name("A1"):
            print("True")
        else:
            print("False")
        print(mg.cast_spell("Lightning", 15))
        print(mg.cast_spell("Lightning", 9))

    main()
