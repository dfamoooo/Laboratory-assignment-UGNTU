"""Скользящие средние: SMA, центрированное MA, EMA + deque-версия и бенчмарк."""
from __future__ import annotations
import time
from collections import deque
from typing import List, Sequence


# ---------------------------------------------------------------------------
# Валидация окна
# ---------------------------------------------------------------------------
def check_window(window: int, n: int) -> None:
    """
    Валидация окна для скользящих средних.

    Требования:
      - window — целое число >= 1
      - window <= n (иначе окно больше ряда)
    """
    if not isinstance(window, int):
        raise TypeError("window должен быть целым числом")
    if window < 1:
        raise ValueError("window должен быть >= 1")
    if window > n:
        raise ValueError(f"window ({window}) не может быть больше длины ряда ({n})")


# ---------------------------------------------------------------------------
# Простая скользящая средняя (SMA) через бегущую сумму
# ---------------------------------------------------------------------------
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





# ---------------------------------------------------------------------------
# Центрированная скользящая средняя 
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# Экспоненциальная скользящая средняя (EMA)
# ---------------------------------------------------------------------------
def exponential_moving_average(data: Sequence[float], alpha: float) -> List[float]:
    """
    Экспоненциальная скользящая средняя (EMA).

    EMA[0] = data[0]
    EMA[i] = alpha * data[i] + (1 - alpha) * EMA[i-1], где 0 < alpha <= 1
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


# ---------------------------------------------------------------------------
# SMA с использованием deque (двусторонней очереди)
# ---------------------------------------------------------------------------
def simple_moving_average_deque(data: Sequence[float], window: int) -> List[float]:
    """SMA с использованием deque (двусторонней очереди)."""
    check_window(window, len(data))

    result = []
    d = deque()
    running_sum = 0.0
    for x in data:
        d.append(x)
        running_sum += x
        if len(d) > window:
            running_sum -= d.popleft()
        if len(d) == window:
            result.append(running_sum / window)
    return result


# ---------------------------------------------------------------------------
# Бенчмарк: сравнение list- и deque-реализаций SMA
# ---------------------------------------------------------------------------
def benchmark_moving_average(
    data: Sequence[float],
    window: int,
    repeats: int = 1000,
) -> dict:
    """
    Замеряет среднее время выполнения SMA для реализаций на list и deque.
    Возвращает словарь с ключами 'list' и 'deque' (время в секундах).
    """
    # Проверка корректности окна (выбросит ValueError при необходимости)
    check_window(window, len(data))

    # Замер для list-реализации (существующая simple_moving_average)
    t0 = time.perf_counter()
    for _ in range(repeats):
        simple_moving_average(data, window)
    t_list = (time.perf_counter() - t0) / repeats

    # Замер для deque-реализации
    t0 = time.perf_counter()
    for _ in range(repeats):
        simple_moving_average_deque(data, window)
    t_deque = (time.perf_counter() - t0) / repeats

    return {"list": t_list, "deque": t_deque}
