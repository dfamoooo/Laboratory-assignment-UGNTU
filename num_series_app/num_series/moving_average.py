from typing import Sequence, List


def check_window(window: int, n: int) -> None:
    """
    Валидация окна для скользящих средних.

    Требования:
      - window — целое число ≥ 1
      - window ≤ n (иначе окно больше ряда)
    """
    if not isinstance(window, int):
        raise TypeError("window должен быть целым числом")
    if window < 1:
        raise ValueError("window должен быть ≥ 1")
    if window > n:
        raise ValueError(f"window ({window}) не может быть больше длины ряда ({n})")


def simple_moving_average(data: Sequence[float], window: int) -> List[float]:
    """
    Простая скользящая средняя (SMA) через бегущую сумму (O(n)).

    Длина результата: len(data) - window + 1.
    """
    n = len(data)
    check_window(window, n)

    # Бегущая сумма по первому окну
    running = sum(data[:window])
    result: List[float] = [running / window]

    # Обновляем сумму, добавляя новый элемент и убирая ушедший из окна
    for i in range(window, n):
        running += data[i] - data[i - window]
        result.append(running / window)

    return result


def centered_moving_average(data: Sequence[float], window: int) -> List[float]:
    """
    Центрированная скользящая средняя.

    Окно должно быть нечётным. Результат выровнен по центру:
    для окна w = 2k+1 значение соответствует позиции k..n-k-1.
    Длина результата: n - window + 1 (как у обычной SMA).
    """
    n = len(data)
    check_window(window, n)

    if window % 2 == 0:
        raise ValueError("Для centered_moving_average окно должно быть нечётным")

    k = window // 2  # смещение до центра

    result: List[float] = []
    for i in range(k, n - k):
        # окно от i-k до i+k включительно (всего window элементов)
        segment = data[i - k:i + k + 1]
        result.append(sum(segment) / window)

    return result


def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """
    Экспоненциальная скользящая средняя (EMA).

    EMA[0] = data[0]
    EMA[i] = alpha * data[i] + (1 - alpha) * EMA[i-1], где 0 < alpha ≤ 1
    """
    if not data:
        return []

    if not (0 < alpha <= 1):
        raise ValueError("alpha должен быть в диапазоне (0, 1]")

    result: List[float] = [float(data[0])]
    prev = result[0]

    for x in data[1:]:
        ema = alpha * x + (1 - alpha) * prev
        result.append(ema)
        prev = ema

    return result
