import math
import random
from typing import List, Optional, Any
def _validate_n(n) -> None:
    """Проверяет, что n — положительное целое число."""
    # 1. Проверка на bool (в Python True == 1, но нам нужен именно int)
    if isinstance(n, bool):
        raise ValueError(f"n должно быть положительным целым числом (получено: {n!r}, причина: bool не является int)")
    
    # 2. Проверка на float, которые являются целыми (например, 3.0)
    if isinstance(n, float) and n.is_integer():
        n = int(n)
    
    # 3. Проверка, что это int (после приведения float выше)
    if not isinstance(n, int):
        raise ValueError(f"n должно быть положительным целым числом (получено: {n!r}, причина: неверный тип {type(n).__name__})")
    
    # 4. Проверка, что n > 0
    if n <= 0:
        raise ValueError(f"n должно быть положительным целым числом (получено: {n!r}, причина: значение <= 0)")






def _validate_seed(seed: Any) -> Optional[int]:
    """
    Проверяет и нормализует seed для random.Random.
    Разрешённые типы: None, int, float, str, bytes, bytearray.
    Явно запрещает bool, чтобы не было сюрпризов.
    Возвращает значение, которое можно безопасно передать в random.Random().
    """
    if seed is None:
        return None

    # Запрещаем bool: в Python bool — подкласс int, но random в новых версиях его отвергает
    if isinstance(seed, bool):
        raise TypeError("seed не должен быть bool; используйте int или None")

    if isinstance(seed, (int, float, str, bytes, bytearray)):
        # random.Random сам умеет работать с этими типами;
        # если хочешь строго int — можно конвертировать float, но это необязательно.
        return seed

    raise TypeError(
        f"seed должен быть одним из: None, int, float, str, bytes, bytearray; "
        f"получено: {type(seed).__name__} ({seed!r})"
    )


def random_series(
    n: int,
    low: float = -100.0,
    high: float = 100.0,
    seed: Optional[Any] = None,
) -> List[float]:
    _validate_n(n)
    if low >= high:
        raise ValueError(f"low должно быть меньше high (получено: {low} >= {high})")

    valid_seed = _validate_seed(seed)
    rng = random.Random(valid_seed)

    return [rng.uniform(low, high) for _ in range(n)]


def sine_series(
    n: int,
    amplitude: float = 1.0,
    frequency: float = 1.0,
    noise: float = 0.0,
    seed: Optional[Any] = None,
) -> List[float]:
    _validate_n(n)

    valid_seed = _validate_seed(seed)
    rng = random.Random(valid_seed)

    return [
        amplitude * math.sin(2 * math.pi * frequency * i / n)
        + (rng.uniform(-noise, noise) if noise else 0.0)
        for i in range(n)
    ]


def trend_series(
    n: int,
    start: float = 0.0,
    step: float = 1.0,
    noise: float = 0.0,
    seed: Optional[Any] = None,
) -> List[float]:
    _validate_n(n)

    valid_seed = _validate_seed(seed)
    rng = random.Random(valid_seed)

    return [
        start + step * i + (rng.uniform(-noise, noise) if noise else 0.0)
        for i in range(n)
    ]
