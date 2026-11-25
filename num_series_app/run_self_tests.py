"""Самодостаточный скрипт с декоратором @check для проверки
ключевых инвариантов без установки pytest"""
"""Автономный запуск проверок без pytest."""
import sys
import traceback


from num_series.generator import random_series, sine_series, trend_series, _validate_n
from num_series.stats import mean, median, spread, summarize
from num_series.moving_average import (
    simple_moving_average,
    centered_moving_average,
    exponential_moving_average,
)

CHECKS = []
FAILED = []


def check(fn):
    """Декоратор: регистрирует функцию как проверку."""
    CHECKS.append(fn)
    return fn


@check
def check_mean():
    assert abs(mean([1, 2, 3]) - 2.0) < 1e-9
    assert abs(mean([0.1, 0.2, 0.3]) - 0.2) < 1e-9


@check
def check_median_outlier():
    assert median([1, 2, 3, 4, 1000]) == 3


@check
def check_sma():
    assert simple_moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]


@check
def check_ema_alpha1():
    data = [1.0, 5.0, -2.0]
    assert exponential_moving_average(data, 1.0) == data


@check
def check_generator_reproducible():
    assert random_series(20, seed=42) == random_series(20, seed=42)


@check
def check_validate_n_rejects_zero():
    try:
        _validate_n(0)
    except ValueError:
        return
    raise AssertionError("_validate_n(0) не выбросил ValueError")


def main() -> int:
    print(f"Запуск {len(CHECKS)} проверок...\n")
    for fn in CHECKS:
        try:
            fn()
            print(f"  [OK]   {fn.__name__}")
        except Exception as exc:
            print(f"  [FAIL] {fn.__name__}: {exc}")
            traceback.print_exc()
            FAILED.append(fn.__name__)
    print(f"\nИтого: {len(CHECKS) - len(FAILED)}/{len(CHECKS)} прошло")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())