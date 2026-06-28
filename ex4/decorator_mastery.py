#!/usr/bin/env python3

from functools import wraps
from typing import Callable
import time
import random


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting function {func.__name__}")
        start = time.perf_counter()
        ret = func(*args, **kwargs)
        end = time.perf_counter()
        print("Spell completed in {:.2f} seconds".format(end - start))
        return ret
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decolator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*arg, **kwargs):
            if arg[-1] >= min_power:
                return func(*arg, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decolator


def retry_spell(max_attempts: int) -> Callable:
    def retry(func: callable) -> Callable:
        @wraps(func)
        def wrapper(*arg, **kwargs):
            for cnt_try in range(1, max_attempts+1):
                try:
                    ret = func(*arg, **kwargs)
                    return ret
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {cnt_try}/{max_attempts})")
                    if cnt_try == max_attempts:
                        return (
                            "Spell casting failed after"
                            " max_attempts attempts")
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
        return f"Successfully cast {spell_name} with <{power}> power"

    @staticmethod
    @spell_timer
    def fireball() -> None:
        print("Testing spell timer...")
        print("Casting fireball...")
        time.sleep(1.23)
        print("Result: Fireball cast!")

    @staticmethod
    @retry_spell(5)
    def waaaaaaagh() -> str:
        i: int = random.randint(0, 9)
        if i % 3 == 0:
            return "Waaaaaaagh spelled !"
        else:
            raise Exception
            return


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
        if mg.validate_mage_name("a"):
            print("True")
        else:
            print("False")
        if mg.validate_mage_name("a b c"):
            print("True")
        else:
            print("False")
        print(mg.cast_spell("iceball", 15))
        print(mg.cast_spell("iceball", 9))

    main()
