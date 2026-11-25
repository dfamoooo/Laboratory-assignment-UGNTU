"""
Вариант 5: ряд из 2000 целых чисел randint(-50, 50).

Показатели:
  - количество отрицательных / нулевых / положительных значений;
  - SMA (реализация на list и на deque) + EMA;
  - краевые случаи k = 1 (результат = исходный ряд) и k = 2.
"""
from __future__ import annotations

import random
import sys
from typing import List

from num_series_app.num_series import (
    simple_moving_average,
    simple_moving_average_deque,
    benchmark_moving_average,
    exponential_moving_average,
)

N = 2000
SEED = 42


def build_series(n: int, seed: int) -> List[int]:
    """Ряд из n целых чисел randint(-50, 50) с фиксированным зерном."""
    rng = random.Random(seed)
    return [rng.randint(-50, 50) for _ in range(n)]


def count_categories(data: List[int]) -> dict:
    """Количество отрицательных / нулевых / положительных значений."""
    neg = sum(1 for x in data if x < 0)
    zero = sum(1 for x in data if x == 0)
    pos = sum(1 for x in data if x > 0)
    return {"neg": neg, "zero": zero, "pos": pos}


def check_edge_case_k1(data: List[int]) -> None:
    """k = 1: обе реализации SMA должны вернуть исходный ряд."""
    sma_list = simple_moving_average(data, 1)
    sma_deque = simple_moving_average_deque(data, 1)
    expected = [float(x) for x in data]
    assert len(sma_list) == len(data), "k=1: длина результата не равна n"
    assert sma_list == expected, "k=1: list-реализация не совпала с исходным рядом"
    assert sma_deque == expected, "k=1: deque-реализация не совпала с исходным рядом"
    print("  k = 1 : OK — результат обеих реализаций равен исходному ряду")


def check_edge_case_k2(data: List[int]) -> None:
    """k = 2: обе реализации должны дать попарное среднее соседних точек."""
    sma_list = simple_moving_average(data, 2)
    sma_deque = simple_moving_average_deque(data, 2)
    expected = [(data[i] + data[i + 1]) / 2 for i in range(len(data) - 1)]
    assert len(sma_list) == len(data) - 1, "k=2: длина результата не равна n - 1"
    assert sma_list == expected, "k=2: list-реализация дала неверное попарное среднее"
    assert sma_deque == expected, "k=2: deque-реализация дала неверное попарное среднее"
    print("  k = 2 : OK — результат равен попарному среднему соседних точек")


def main() -> int:
    data = build_series(N, SEED)

    print("=" * 60)
    print(f"Вариант 5: n={N}, randint(-50, 50), seed={SEED}")
    print("=" * 60)

    # --- 1. Дополнительный показатель ---
    cats = count_categories(data)
    print("Количество значений:")
    print(f"  отрицательных : {cats['neg']}")
    print(f"  нулевых       : {cats['zero']}")
    print(f"  положительных : {cats['pos']}")
    print(f"  (сумма = {cats['neg'] + cats['zero'] + cats['pos']})")

    # --- 2. Скользящие средние ---
    alpha = 0.3
    sma_list = simple_moving_average(data, 10)
    sma_deque = simple_moving_average_deque(data, 10)
    ema = exponential_moving_average(data, alpha)

    assert sma_list == sma_deque, "SMA list и deque дали разные результаты"
    print(f"\nSMA (k=10): len={len(sma_list)}, list и deque совпадают")
    print(f"  первые 5 значений SMA: {[round(v, 3) for v in sma_list[:5]]}")
    print(f"EMA (alpha={alpha}): len={len(ema)}")
    print(f"  первые 5 значений EMA: {[round(v, 3) for v in ema[:5]]}")

    # --- 3. Краевые случаи ---
    print("\nКраевые случаи:")
    check_edge_case_k1(data)
    check_edge_case_k2(data)

    # --- 4.  бенчмарк обеих реализаций ---
    timings = benchmark_moving_average(data, 10, repeats=1000)
    print("\nБенчмарк SMA (среднее за 1000 повторов):")
    print(f"  list  : {timings['list']:.8f} с")
    print(f"  deque : {timings['deque']:.8f} с")
    print(f"  отношение (list/deque): {timings['list'] / timings['deque']:.2f}")

    print("=" * 60)
    return 0


if __name__ == "__main__":
    sys.exit(main())
