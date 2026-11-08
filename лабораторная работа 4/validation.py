"""
Валидация пользовательского ввода.
- Проверка границ через if-elif-else.
- Циклический ввод до корректного значения.
"""

from __future__ import annotations

from constans import U_MIN, U_MAX, I_MIN, I_MAX
from logger import log_error


def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    
    """Проверка попадания value в [low, high] через if-elif-else
    :return: (True, "") или (False, сообщение)"""

    if value < low:
        return False, f"Ошибка: значение меньше нижней границы ({low})."
    elif value > high:
        return False, f"Ошибка: значение больше верхней границы ({high})."
    else:
        return True, ""


def input_number(prompt: str, low: float, high: float) -> float:
    """
    Циклически запрашивать число, пока не будет корректного
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Ошибка: введено не число ('{raw}'). {msg}"
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        print(msg + " Повторите ввод.")
        log_error(msg)


def input_voltage() -> float:
    """Циклический ввод напряжения U (от 12 до 1000)"""
    return input_number(
        "Введите напряжение U, В (12..1000): ",
        U_MIN, U_MAX,
    )


def input_current() -> float:
    """Циклический ввод тока I (от 0.1 до 500)"""
    return input_number(
        "Введите ток I, А (0.1..500): ",
        I_MIN, I_MAX,
    )